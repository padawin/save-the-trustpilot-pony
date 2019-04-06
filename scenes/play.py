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
