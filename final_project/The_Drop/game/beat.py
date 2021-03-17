# Represents one of the beat objects crossing the screen. Should have a constant velocity,
# a starting y-position that makes it reach the DropPoint at the right time, an x-value that
# makes it travel in the correct column, and an attribute to track what key it is bound to.
import arcade
from game import constants

class Beat(arcade.Sprite):

    def __init__(self, beat, time):
        """Initialize the game
        """
        super().__init__(constants.DIRROOT + "/images/beat.png")

        #this will only work for one player mode. 
        if beat == 'q':
            self.center_x = constants.BEAT_X_1
        if beat == 'w':
            self.w_center_x = constants.BEAT_X_2
        if beat == 'e':
            self.e_center_x = constants.BEAT_X_3 
        if beat =='r':
            self.r_center_x = constants.BEAT_X_4
        
        self.starting_y = constants.DROP_POINT_Y + (time * constants.BEAT_SPEED)
        self.velocity = constants.BEAT_SPEED

    def hit(self):
        pass

    def kill(self):
        pass