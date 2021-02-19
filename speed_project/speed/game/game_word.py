import random
from game.actor import Actor
from game.point import Point
from game import constants
class Game_word(Actor):
    
    def __init__(self, sector):
        '''
        Game_word class constructor. Inherits from Actor class.
        Sets the text and moves the food to different, random positions within
        the game board in the terminal.

        Args:
            self(Actor): an instance of Actor
        '''
        super().__init__()
        velocity = Point(1, 0)
        self.set_velocity(velocity)
        self.reset(sector)

    def get_points(self):
        '''
        Gets the points for when the user guesses the word

        Args:
            self(Food): an instance of Food

        Returns:
            integer: The points each food is worth
        '''
        return self._points

    def reset(self, sector):
        '''
        sets the words 

        Args:
            self(_word): chooses a word that will spawn
            self(_points): registers length of word for the boundry
            self(set_text): for creation of words
            self(set_position): 
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
        return self._word
