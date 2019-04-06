import pygame


class Game:
    def __init__(self):
        self._scene = None
        self._continue = True
        self._needs_redraw = True

    def set_scene(self, scene):
        self._scene = scene

    def update(self):
        for event in pygame.event.get():
            if (
                event.type == pygame.QUIT
                or event.type == pygame.KEYDOWN
                and event.key == pygame.K_ESCAPE
            ):
                self._continue = False
                return
            else:
                self._scene.handle_event(event)
        self._scene.update(self)

    def render(self, screen):
        if self._needs_redraw:
            self._scene.render(screen)
            pygame.display.update()
            self._needs_redraw = False

    def finished(self):
        return not self._continue
