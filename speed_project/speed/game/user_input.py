from game.actor import Actor
from game.point import Point
from game import constants


class User_input(Actor):
    """Holds informmation that the user inputs

    Stereotype: Information holder.

    Attributes:
        _current_input (string): The completed word the user is typing
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args
            self (user_imput): an instance of user_imput
        """
        self._current_input = ""
        self.set_text(self._current_input)
        x = 0
        y = constants.MAX_Y
        position = Point(x, y)
        self.set_position(position)

    def set_input_word(self, input_letter):
        """ Defines the complete input in string form letter by letter

        Args:
            self (user_imput): an instance of user_imput
            input_letter: the user's most recently typed/letter to add
        """
        self._current_input += input_letter
        self.set_text(self._current_input)

    def get_input_word(self):
        """ returns the complete input in string form

        Args:
            self (user_imput): an instance of user_imput
        Returns:
            the previous_input as a string
        """
        return self._current_input

    def clear(self):
        """ Defines the complete input in string form letter by letter

        Args:
            self (user_imput): an instance of user_imput
        """
        self._current_input = ""
        self.set_text("")

    def delete_last_char(self):
        """ Deletes the last letter in the user inputted word, and removes the left carrot.

        Args:
            self (user_imput): an instance of user_imput
        """
        self._current_input = self._current_input[:-2]
        self.set_text(self._current_input)
