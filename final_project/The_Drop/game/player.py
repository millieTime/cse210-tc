# Keeps track of player information. Specifically useful when we implement
# multiplayer. Should know the player's score (likely a Score object), which
# keys they are supposed to press.
from game.score import Score
from game import constants
import arcade

class Player(arcade.Sprite):

    def __init__(self, player_name, keys, max_score):
        super().__init__()
        self._player_name = player_name
        self._keys = keys
        self._score = Score(max_score)
        self._right = constants.MAX_X - 20

    def draw(self):
        arcade.draw_text(text=str(self), start_x=self._right, start_y=25, color=arcade.color.ALLOY_ORANGE, font_size=20, anchor_x='right')

    def set_player_name(self, name):
        self._player_name = name

    def get_player_name(self):
        return self._player_name

    def add_points(self, points = 5):
        self._score.add_points(points)

    def subtract_points(self, points = 5):
        self._score.subtract_points(points)

    def get_score(self):
        return self._score.get_total_points()

    def set_player_keys(self, keys):
        self._keys = keys

    def get_player_keys(self):
        return self._keys

    def get_accuracy(self):
        return self._score.get_accuracy()

    def reset_score(self):
        self._score.reset_score()

    def __str__(self):
        return f'{self._player_name}, {self._score}'
