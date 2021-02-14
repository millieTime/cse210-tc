class Guess:
    """Holds informmation about a guess

    Stereotype: Information holder.

    Attributes:
        guess (string): the guess to hold
    """
    def __init__(self, guess):
        """Class constructor. Declares and initializes instance attributes.

        Args
            self (Guess): an instance of Guess
            guess (string): the string to create the guess about
        """
        self._guess = guess
    
    def get_guess(self):
        """ returns the guess in string form

        Args:
            self (Guess): an instance of Guess
        
        Returns:
            the guess as a string
        """
        return self._guess