# Represents one of the beat objects crossing the screen. Should have a constant velocity,
# a starting y-position that makes it reach the DropBar at the right time, an x-value that
# makes it travel in the correct column, and an attribute to track what key it is bound to.
import os
import arcade
from game import constants

PATH = os.path.dirname(os.path.abspath(__file__))

class Beat(arcade.Sprite):

    def __init__(self, beat, time):
        """Initialize the game
        """
        super().__init__(PATH + "/assets/images/beat_1.png", constants.SCALING/2)
        
        """Adds a new beat to the screen

        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """

        # Set its position to a random height and off screen right
        beat.left = constants.BEAT_X[beat]
        beat.top =  self.height + time

        # Set its speed to a random speed heading left
        beat.velocity = constants.BEAT_SPEED

    def kill(self):
        pass
        
