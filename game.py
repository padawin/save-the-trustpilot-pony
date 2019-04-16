import pygame


class Game:
    """
    Class managing the scenes and their update.
    """

    def __init__(self):
        self._scene = None
        self._continue = True
        self._needs_redraw = True

    def set_scene(self, scene):
        self._scene = scene

    def update(self):
        """
        Handle the events, then update the current scene.

        Capture any event from Pygame. If there are any, the scene is asked to
        handle them. Then the scene is updated.
        """
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
        self._needs_redraw = self._scene.update()

    def render(self, screen):
        """
        Render the scene if it needs rendering.

        If the scene has not been updated, no rendering is needed.
        """
        if self._needs_redraw:
            self._scene.render(screen)
            pygame.display.update()
            self._needs_redraw = False

    def finished(self):
        return not self._continue
