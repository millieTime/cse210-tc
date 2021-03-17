# Represents one of the beat objects crossing the screen. Should have a constant velocity,
# a starting y-position that makes it reach the DropPoint at the right time, an x-value that
# makes it travel in the correct column, and an attribute to track what key it is bound to.
import arcade
from game import constants

class Beat(arcade.Sprite):

    def __init__(self, beat, time):
        """Initialize the game
        """
        x = 0
        img = ""
        if beat == 'q':
            x = constants.BEAT_X_1
            img = constants.Q_IMAGE
        elif beat == 'w':
            x = constants.BEAT_X_2
            img = constants.W_IMAGE
        elif beat == 'e':
            x = constants.BEAT_X_3 
            img = constants.E_IMAGE
        elif beat =='r':
            x = constants.BEAT_X_4
            img = constants.R_IMAGE

        super().__init__(img, scale=constants.BEAT_SCALE)
        self.center_x = x
        self.center_y = constants.DROP_POINT_Y - (time * constants.BEAT_SPEED) + self.height
        self.change_y = constants.BEAT_SPEED

    def hit(self):
        pass

    def kill(self):
        pass