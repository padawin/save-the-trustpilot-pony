class MazeCreationError(Exception):
    def __init__(self, e):
        super().__init__(f"An error occured while creating the maze: {e}")


class InvalidMazeDataError(Exception):
    pass


class InvalidConfigError(Exception):
    def __init__(self):
        super().__init__("Stop messing around with the configuration")
