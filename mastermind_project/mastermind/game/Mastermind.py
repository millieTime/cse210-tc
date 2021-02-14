import random

class Mastermind:
    """A code template for a code master. Its responsibility is to generate codes and create hints.

    Stereotype: Information holder.
    
    Attributes:
        _items (dictionary): a dictionary of lists, one per player, that keeps track of the code,
                             the player's most recent guess, and the hint for that guess.
    """


    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Mastermind): An instance of Mastermind.
            self._items: An empty dictionary/object that will eventually store a key === playerName and a list of vlaues ===
                         [generated secret code, player most recent guess, and hint once comparing the code and guess]
        """
        self._items = {}

    def prepare(self, player):
        """Sets up the mastermind with an entry for each player.

        Args:
            self (Mastermind): an instance of Mastermind.
        """
        name = player.get_name()
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]

    def make_guess(self, player, guess):
        """Updates _items for the given player and guess. Makes a new hint.

        Args:
            self (Mastermind): an instance of Mastermind.
            player (Player): the player whose hint and guess to update.
            guess (Guess): the guess to make.
        """
        items = self._items[player.get_name()]
        items[1] = guess.get_guess()
        items[2] = self._create_hint(items[0], guess.get_guess())
        self._items[player.get_name()] = items

    def get_hint(self, player):
        """ return the most recent hint for the given player.

        Args:
            self (Mastermind): an instance of Mastermind.
            player (Player): the player whose hint to return.
        
        Returns:
            the most recent hint for the given player.
        """
        return self._items[player.get_name()][2]


    def to_string(self):
        """
        Converts the game data to its string representation and returns it to the caller

        Args:
        - self: an instance of Mastermind

        Returns:
            a string representation of the Mastermind object.
        """
        text = '\n-------------------------'
        text += '\n'
        for key, value in self._items.items():
            text += 'Player ' + key + ': ' + value[1]
            text += ''
            text += ', ' + value[2]
            text += '\n'
        text += '-------------------------\n'
        return text

    def _create_hint(self, code, guess):
        """Generates a hint based on the given code and guess.

        Args:
            self (Mastermind): An instance of Mastermind.
            code (string): The code to compare with.
            guess (string): The guess that was made.

        Returns:
            string: A hint in the form [xxxx]
        """
        hint = ""
        for index, letter in enumerate(guess):
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return hint

    def has_won(self, player):
        """ checks if the given player has won

        Args:
            self (Mastermind): an instance of a mastermind
            player (Player): The player for whom we are checking for a win.

        Returns:
            (boolean) True if the player has won, False otherwise.
        """
        hint = self._items[player.get_name()][2]
        print(hint)
        for symbol in hint:
            if symbol != "x":
                print("Failure:", symbol)
                return False
        return True