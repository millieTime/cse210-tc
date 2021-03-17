# Represents one of the beat objects crossing the screen. Should have a constant velocity,
# a starting y-position that makes it reach the DropPoint at the right time, an x-value that
# makes it travel in the correct column, and an attribute to track what key it is bound to.
import arcade
from game import constants

class Beat(arcade.Sprite):

    def __init__(self, beat, time):
        """Initialize the game
        """
        super().__init__(constants.BEAT_IMAGES[beat], scale=constants.BEAT_SCALE)
        self.center_x = constants.BEAT_X[beat]
        self.center_y = constants.DROP_POINT_Y - (time * constants.BEAT_SPEED) + self.height
        self.change_y = constants.BEAT_SPEED

    def kill(self):
        # Do something when the brick dies
        pass
