import random


class Mastermind:

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Mastermind): An instance of Mastermind.
            self._items: An empty dictionary/object that will eventually store a key === playerName and a list of vlaues ===
                         [generated secret code, player most recent guess, and hint once comparing the code and guess]
        """
        self._items = {}

    def prepare(self, player):
        """Sets up the board with an entry for each player.

        Args:
            self (Board): an instance of Board.
        """
        name = player.get_name()
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]

    def to_string(self):
        """
        Converts the game data to its string representation and returns it to the caller

        Args:
        - self: an isntance of Mastermind()
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
