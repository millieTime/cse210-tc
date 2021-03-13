# Represents one of the beat objects crossing the screen. Should have a constant velocity,
# a starting y-position that makes it reach the DropBar at the right time, an x-value that
# makes it travel in the correct column, and an attribute to track what key it is bound to.
import os
import arcade
import game.constants

PATH = os.path.dirname(os.path.abspath(__file__))

class Beat(arcade.Sprite):

    def __init__(self, beat, time):
        """Initialize the game
        """
        super().__init__()
        
        self.constants = game.constants

        #this will only work for one player mode. 
        """   if beat == 'q':
            self.center_x = constants.BEAT_X_1
        if beat == 'w':
            self.w_center_x = constants.BEAT_X_2
        if beat == 'e':
            self.e_center_x = constants.BEAT_X_3 
        if beat =='r':
            self.r_center_x = constants.BEAT_X_4  """
        
        self.starting_y = constints.DROP_POINT_Y + (time * constants.BEAT_SPEED)
    def add_beat(self, beat, delta_time: float):
            """Adds a new beat to the screen

            Arguments:
                delta_time {float} -- How much time has passed since the last call
            """
            if beat == 'q':
                self.beat.x = constants.BEAT_X_1
            if beat == 'w':
                self.beat.x = constants.BEAT_X_2
            if beat == 'e':
                self.beat.x = constants.BEAT_X_3 
            if beat =='r':
                self.beat.x = constants.BEAT_X_4

            # First, create the new beat sprite
            beat = FlyingSprite(PATH + "/images/beat.png", SCALING)

            # Set its position to a random height and off screen right
            beat.x = constants.BEAT_X_1
            beat.y = constants.MAX_Y + 10

            # Set its speed to a random speed heading left
            beat.velocity = bpm

            # Add it to the enemies list
            self.beats_list.append(beat)
            self.all_sprites.append(beat)


    def hit(self):
        pass

    def kill(self):
        pass
