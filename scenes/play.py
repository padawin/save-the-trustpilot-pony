import pygame

import config
from exceptions import InvalidMazeDataError, InvalidConfigError

from .scene import Scene
from trustpilot import TrustPilot


class PlayScene(Scene):
    def __init__(self):
        self._images_cache = {
            "pony": pygame.image.load(config.PONY_IMAGE),
            "domokun": pygame.image.load(config.DOMOKUN_IMAGE),
            "end-point": pygame.image.load(config.END_IMAGE)
        }
        self._direction = None
        try:
            self._maze_id = TrustPilot.create_maze(config.MAZE_INFO)
        except InvalidMazeDataError:
            raise InvalidConfigError()
        else:
            self._maze_data = None
            self._update_maze()

    def _update_maze(self):
        self._maze_data = TrustPilot.get_maze(self._maze_id)
        self._needs_redraw = True

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self._direction = "north"
            elif event.key == pygame.K_RIGHT:
                self._direction = "east"
            elif event.key == pygame.K_DOWN:
                self._direction = "south"
            elif event.key == pygame.K_LEFT:
                self._direction = "west"

    def update(self):
        if self._direction is not None:
            TrustPilot.move(self._maze_id, self._direction)
            self._update_maze()
            self._direction = None
            return True
        return False

    def _get_walls(self, cell_index):
        walls = self._maze_data["data"][cell_index]
        maze_width = self._maze_data["size"][0]
        try:
            neighbour_south = self._maze_data["data"][
                cell_index + maze_width
            ]
        except IndexError:  # the cell is on the bottom line
            neighbour_south = {"north"}
        finally:
            if "north" in set(neighbour_south):
                walls.append("south")
        if (cell_index + 1) % maze_width > 0:
            neighbour_east = self._maze_data["data"][cell_index + 1]
        else:  # the cell is on the right column
            neighbour_east = {"west"}

        if "west" in set(neighbour_east):
            walls.append("east")
        return walls

    def _get_cell_image(self, sides):
        flags = {
            "west": 0x1,
            "south": 0x2,
            "east": 0x4,
            "north": 0x8
        }
        image_idx = 0
        for side in sides:
            image_idx |= flags[side]

        try:
            image = self._images_cache[image_idx]
        except KeyError:
            self._images_cache[image_idx] = image = pygame.image.load(
                config.IMAGE_PATTERN.format(image_idx)
            )
        finally:
            return image

    def render(self, screen):
        maze_width = self._maze_data["size"][0]
        maze_height = self._maze_data["size"][1]
        cell_width = config.CELL_PIXELS_SIZE[0]
        cell_height = config.CELL_PIXELS_SIZE[1]
        maze_surface = pygame.Surface(
            (cell_width * maze_width, cell_height * maze_height)
        )
        self._render_maze(maze_surface)
        for actor in ("pony", "domokun", "end-point"):
            self._render_actor(maze_surface, actor)
        screen.blit(
            pygame.transform.scale(maze_surface, config.WINDOW_SIZE),
            (0, 0)
        )

    def _render_maze(self, maze_surface):
        maze_width = self._maze_data["size"][0]
        cell_width = config.CELL_PIXELS_SIZE[0]
        cell_height = config.CELL_PIXELS_SIZE[1]
        for index, _ in enumerate(self._maze_data["data"]):
            walls = self._get_walls(index)
            image = self._get_cell_image(walls)
            maze_surface.blit(
                image,
                (
                    cell_width * (index % maze_width),
                    cell_height * (index // maze_width)
                )
            )

    def _render_actor(self, maze_surface, actor):
        maze_width = self._maze_data["size"][0]
        cell_width = config.CELL_PIXELS_SIZE[0]
        cell_height = config.CELL_PIXELS_SIZE[1]
        for actor_index in self._maze_data[actor]:
            maze_surface.blit(
                self._images_cache[actor],
                (
                    cell_width * (actor_index % maze_width),
                    cell_height * (actor_index // maze_width)
                )
            )
