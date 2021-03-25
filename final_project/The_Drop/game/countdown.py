import arcade
from game import constants

class Countdown(arcade.Sprite):
    # want this to show 3, 2, 1, so I'll need to override update and increment some timer to keep track of the number here.
    # Won't have pictures so much as it will have text that starts big and gets small.
    def __init__(self):
        # add 3, 2, 1 images
        super().__init__(constants.CDIMAGE_1)
        self.append_texture(constants.CDIMAGE_2)
        self.append_texture(constants.CDIMAGE_3)
        self._known_time = 0
        self._time = 0
        self.change_x = 1
        self.center_x = constants.MAX_X / 2

    def update(self):
        """Update the position of the sprite
        When it moves off screen to the left, remove it
        """
        # 'Move' the sprite
        super().update()
        # And now, turn that movement into time
        self.time += self.center_x - constants.MAX_X / 2
        self.center_x = constants.MAX_X / 2
        if self._time // 1 > self._known_time:
            self._known_time = self._time // 1
            self.set_texture(self._known_time)

