# Might be really similar to the _input_service. idk. It needs to be able to
# get keyboard inputs from the user when the game is running, and later when
# we do level selection we'll probably want the user to be able to click on
# the levels.
from game.point import Point

import arcade

class Input:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _keys (list): up, dn, lt, rt.
    """

    def __init__(self, watch_keys):
        """The class constructor."""
        self._keys_pressed = {}
        for key in watch_keys:
            self.keys_pressed[key] = False
    
    def set_key(self, key, modifiers):
        #Ignoring modifies ar this point...
        print(key)
        if key in self._keys_pressed.keys():
            self._keys_pressed[key] = True

    def remove_key(self, key, modifiers):
        if key in self._keys_pressed.keys():
            self._keys_pressed[key] = False

    def pressed_keys(self):
        """Gets the currently pressed keys.

        Returns:
            List: all the keys currently pressed.
        """
        key_list = []
        for key in self._keys_pressed.keys():
            if self._keys_pressed[key]:
                key_list.append(key)
        return key_list
        
    def released_keys(self):
        """Gets the not-pressed keys.

        Returns:
            List: all the keys not currently pressed.
        """
        key_list = []
        for key in self._keys_pressed.keys():
            if not self._keys_pressed[key]:
                key_list.append(key)
        return key_list