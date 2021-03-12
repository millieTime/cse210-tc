import sys
from game.point import Point
import arcade


class input:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _keys (list): Points for up, dn, lt, rt.
    """

    def __init__(self, screen):
        """The class constructor."""
        
        
    def get_input(self):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """
        beat
        if (
            symbol == arcade.key.Q
        ):
            beat =  "q"

        if (
            symbol == arcade.key.J
            or symbol == arcade.key.L
            or symbol == arcade.key.LEFT
            or symbol == arcade.key.RIGHT
        ):
            self.player.change_x = 0
        return beat
=======
# Might be really similar to the _input_service. idk. It needs to be able to
# get keyboard inputs from the user when the game is running, and later when
# we do level selection we'll probably want the user to be able to click on
# the levels.
