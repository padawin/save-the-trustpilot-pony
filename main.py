import pygame

import config
from scenes.scene import Scene
from game import Game


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode(config.WINDOW_SIZE)

    game = Game()
    game.set_scene(Scene())
    while not game.finished():
        game.update()
        game.render()
