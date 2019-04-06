import pygame

import config
from scenes.scene import Scene
from game import Game


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode(
        [
            map_coord * pixels
            for map_coord, pixels in zip(
                config.MAZE_SIZE, config.CELL_PIXELS_SIZE
            )
        ]
    )

    game = Game()
    game.set_scene(Scene())
    while not game.finished():
        game.update()
        game.render()
