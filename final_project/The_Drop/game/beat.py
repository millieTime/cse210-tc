# Represents one of the beat objects crossing the screen. Should have a constant velocity,
# a starting y-position that makes it reach the DropPoint at the right time, an x-value that
# makes it travel in the correct column, and an attribute to track what key it is bound to.
import arcade
from game import constants

class Beat(arcade.Sprite):

    def __init__(self, key, time):
        super().__init__(constants.BEAT_IMAGE)
        self._key = key
        self._time = time
        self.change_y = 1