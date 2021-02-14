class Player:
    """A person taking part in a game. The responsibility of Player is to keep track of their identity.
    
    Stereotype: 
        Information Holder

    Attributes:
        _name (string): The player's name.
        _guess (Guess): The player's most recent guess.
    """
    def __init__(self, name):
        """The class constructor.
        
        Args:
            self (Player): an instance of Player.
        """
        self._name = name

    def set_guess(self, guess):
        """ sets the player's most recent guess.

        Args:
            self (Player): an instance of Player.
            guess (Guess): the newest guess.
        """
        self._guess = guess

    def get_guess(self):
        """ returns the player's most recent guess.

        Args:
            self (Player): an instance of Player.
        
        returns:
            the player's most recent guess.
        """
        return self._guess

    def get_name(self):
        """Returns the player's name.

        Args:
            self (Player): an instance of Player.
        """
        return self._name