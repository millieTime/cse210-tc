# Tracks a score. Can be read, added to, and contain a multiplyer.
class Score:

    def __init__(self, max_score):
        self._score = 0
        self._max_score = max_score
        self._accuracy = 0

    def add_points(self, points):
        self._score += points

    def subtract_points(self, points):
        self._score -= points

    def reset_score(self):
        self._score = 0

    def get_total_points(self):
        return self._score
    
    def get_accuracy(self):
        # (max_score + player_score ) / (max_score * 2) = hit ratio
        return self._score / self._max_score

    def __str__(self):
        return f'{self._score}'
