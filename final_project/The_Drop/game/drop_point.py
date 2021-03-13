# represents a section of the bottom drop point. 
# If activated, we can check if it's colliding with
# any of the beats, and then award points and remove
# them. If not, the player loses points.

import arcade
from game import constants

class DropPoint(arcade.Sprite):

    def __init__(self, key):
        # no image yet, but when we have one we'll send it here.
        super().__init__(constants.DROP_POINT_IMAGE)
        # Uncomment the following line when we have images.
        self.append_texture(arcade.load_texture(constants.DROP_POINT_IMAGE_2))
        self._key = key
        self._activated = False
        # Don't know what they are in constants, so we'll update
        # this when that's merged.
        if key == 'q':
            self.center_x = constants.BEAT_X_1
        elif key == 'w':
            self.center_x = constants.BEAT_X_2
        elif key == 'e':
            self.center_x = constants.BEAT_X_2
        elif key == 'r':
            self.center_x = constants.BEAT_X_3
        self.center_y = constants.DROP_POINT_Y

    def activate(self):
        self._activated = True
        # change the appearance
        self.set_texture(1)

    def deactivate(self):
        self.activated = False
        # change the appearance
        self.set_texture(0)