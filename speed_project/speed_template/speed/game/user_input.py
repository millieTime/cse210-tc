from game.actor import Actor
from game.point import Point
from game import constants
class User_input(Actor):
    """Holds informmation that the user inputs

    Stereotype: Information holder.

    Attributes:
        input_word (string): The completed word the user is typing
    """
    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args
            self (user_imput): an instance of user_imput
            input_word (string): The string to create the users complete word. 
        """
        self._current_input = ""
        self.set_text(self._current_input)
        x = 0
        y = constants.MAX_Y
        position = Point(x, y)
        self.set_position(position)


    def set_input_word(self,input_letter):
        """ returns the complete input in string form

        Args:
            self (user_imput): an instance of user_imput
        
        Returns:
            the user_imput as a string
        """
        self._current_input += input_letter
        self.set_text(self._current_input)

    def get_input_word(self):
        """ returns the complete input in string form

        Args:
            self (user_imput): an instance of user_imput
            previous_input: a temparary instance of _current_input in order to reset _current_input
        Returns:
            the previous_input as a string
        """
        return self._current_input
    
    def clear(self):
        self._current_input = ""
        self.set_text("")