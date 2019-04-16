class Scene:
    """
    A Scene in a moment in the lifetime of the application.

    For example a configuration menu to choose the difficulty, or the pony name
    could be done as a scene.

    Or once the the pony found the flag :-) or the Domokun :-( a new scene (end
    game) could be loaded to display an end game message.
    """

    def handle_event(self, event):
        pass

    def update(self, game):
        pass

    def render(self, screen):
        pass

    @staticmethod
    def _text_objects(text, font, color):
        """
        Create a surface and a rectangle for the given text, font, and color.
        """
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()
