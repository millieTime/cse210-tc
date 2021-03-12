# represents a section of the bottom drop bar. 
# If activated, we can check if it's colliding with
# any of the beats, and then award points and remove
# them. If not, the player loses points.

import arcade
from game import constants

class DropBar(arcade.Sprite):

    def __init__(self, key):
        # no image yet, but when we have one we'll send it here.
        super().__init__(constants.DROP_BAR_IMAGE)
        # Uncomment the following line when we have images.
        self.append_texture(arcade.load_texture(constants.DROP_BAR_IMAGE_2))
        self._key = key
        self._activated = False
        # Don't know what they are in constants, so we'll update
        # this when that's merged.
        if key == 'q':
            self.center_x = constants.xq
        elif key == 'w':
            self.center_x = constants.xw
        elif key == 'e':
            self.center_x = constants.xe
        elif key == 'r':
            self.center_x = constants.xr
        self.center_y = constants.drop_y

    def activate(self):
        self._activated = True
        # change the appearance
        self.set_texture(1)

    def deactivate(self):
        self.activated = False
        # change the appearance
        self.set_texture(0)