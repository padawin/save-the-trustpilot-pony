class Scene:
    def handle_event(self, event):
        pass

    def update(self, game):
        pass

    def render(self, screen):
        pass

    @staticmethod
    def _text_objects(text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()
