import random
from game.actor import Actor
from game.point import Point
from game import constants
class Game_word(Actor):
    """Represents a word for the user to type. It moves to the right, and can
    bet reset when necessary.

    Stereotype: Information Holder

    Attributes:
        _points (integer): the point value of the word. Also the length.
        _word (string): the word the user has to type.
    """


    
    def __init__(self, sector):
        '''
        Game_word class constructor. Inherits from Actor class.
        Sets the velocity of the word, and other important
        attributes.

        Args:
            self(Actor): an instance of Actor
            sector(integer): the section of screen this word exists in.
        '''
        super().__init__()
        velocity = Point(1, 0)
        self.set_velocity(velocity)
        self.reset(sector)

    def get_points(self):
        '''
        Gets the points for when the user types the word

        Args:
            self(Game_word): an instance of Game_word

        Returns:
            integer: The points this word is worth
        '''
        return self._points

    def reset(self, sector):
        '''
        sets text, points, word, and position.

        Args:
            sector (integer): which fifth of the screen to start in.
        '''
        self._word = random.choice(constants.LIBRARY)
        self._points = len(self._word)
        self.set_text(self._word)
        x = random.randint(1, 10)
        row_min = (constants.MAX_Y - 2) * sector // 5
        row_max = (constants.MAX_Y - 2) * (sector + 1) // 5 - 1
        y = random.randint(row_min, row_max)
        position = Point(x, y)
        self.set_position(position)
    
    def get_word(self):
        """
        returns the word this Game_Word represents.

        Args:
            self (Game_word): an instance of the class Game_word

        Returns:
            string: the word this Game_word represents.
        """
        return self._word
