import pygame

import config
from scenes.play import PlayScene
from game import Game

from exceptions import InvalidConfigError


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode(config.WINDOW_SIZE)
    clock = pygame.time.Clock()

    game = Game()
    try:
        game.set_scene(PlayScene())
    except InvalidConfigError as e:
        print(e)
    else:
        while not game.finished():
            game.update()
            game.render(screen)
            clock.tick(60)
