# level.py
from Code import entity


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[entity] = []

    def run(self, ):
        pass
