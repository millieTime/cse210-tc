# Keeps track of player information. Specifically useful when we implement
# multiplayer. Should know the player's score (likely a Score object), which
# keys they are supposed to press.

import os


class Player:

    def __init__(self, player_name, keys):
        self._player_name = player_name
        self._keys = keys
        self._score = 0

    def set_player_name(self, name):
        self._player_name = name

    def get_player_name(self):
        return self._player_name

    def add_points(self):
        self._score += 5

    def subtract_points(self):
        self._score -= 5

    def get_score(self):
        return self._score

    def set_player_keys(self, keys):
        self._keys = keys

    def get_player_keys(self):
        return self._keys

    def reset_score(self):
        self._score = 0
