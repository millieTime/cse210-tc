# This is the director class
from game.wordhandler import WordHandler

"""
Classes:
 - Director
 - Console (To print and receive inputs) // Austin
 - WordHandler/Finx // Matthew 
 - Parachute // Preston
"""


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.

    Attributes:
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        self.wordhandler = WordHandler()

    def drawWord(self):
        getWord = self.wordhandler.getWord()
        print(getWord)
