<<<<<<< HEAD
import sys
from game.point import Point
from asciimatics.event import KeyboardEvent

class InputServiceAscii:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _keys (list): Points for up, dn, lt, rt.
    """

    def __init__(self, screen):
        """The class constructor."""
        self._screen = screen
        self._keys = {}
        self._keys[119] = Point(0, -1) # w
        self._keys[115] = Point(0, 1) # s
        self._keys[97] = Point(-1, 0) # a
        self._keys[100] = Point(1, 0) # d
        
    def get_direction(self):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """
        direction = Point(0, 0)
        event = self._screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code == 27:
                sys.exit()
            direction = self._keys.get(event.key_code, Point(0, 0))
        return direction
=======
# Might be really similar to the _input_service. idk. It needs to be able to
# get keyboard inputs from the user when the game is running, and later when
# we do level selection we'll probably want the user to be able to click on
# the levels.
>>>>>>> 4a360bf882617995ab2d236c8a4a03f7d23cbde3
