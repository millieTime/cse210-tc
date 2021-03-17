# Tracks a score. Can be read, added to, and contain a multiplyer.

import os


class Score:

    def __init__(self):
        self._score = 0

    def add_points(self):
        self._score += 5

    def subtract_points(self):
        self._score -= 5

    def reset_score(self):
        self._score = 0

    def get_total_points(self):
        return self._score

    def __str__(self):
        return f'{self._score}'
