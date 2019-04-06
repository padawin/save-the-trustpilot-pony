import pygame

import config
from exceptions import InvalidMazeDataError, InvalidConfigError

from .scene import Scene
from trustpilot import TrustPilot


class PlayScene(Scene):
    def __init__(self):
        try:
            self._maze_id = TrustPilot.create_maze(config.MAZE_INFO)
        except InvalidMazeDataError:
            raise InvalidConfigError()
        else:
            self._maze_data = None
            self._update_maze()

    def _update_maze(self):
        self._maze_data = TrustPilot.get_maze(self._maze_id)
