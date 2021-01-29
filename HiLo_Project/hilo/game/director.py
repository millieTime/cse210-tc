# This is the director class
from game.drawer import Drawer

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
        self.keep_playing = True
        self.score = 300
        self.drawer = Drawer()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.acquire_guess()
            self.evaluate_guess()
            keep_playing = self.score > 0 and self.user_play_again()

    def acquire_guess(self):
        """Causes a new card to be drawn, displays it,
        and gets the user's guess.

        Args:
            self (Director): an instance of Director.
        """
        self.drawer.draw_new_card()
        print("The card is:", self.getCurrentCard())
        self.guess = self.getUserInput()
    
    def evaluate_guess(self):
        """Causes a new card to be drawn and displays it.
        Updates the score and displays it.

        Args:
            self (Director): an instance of Director.
        """
        self.drawer.draw_new_card()
        print("Next card was:", self.getCurrentCard())
        comparison = self.compare_inputs(self.guess)
        self.update_points(comparison)
        print("Your score is:", self.score)

    def getUserInput(self):
        userInput = input("Higher or Lower?: ")
        if (userInput == 'Higher' or userInput == 'higher'):
            return True
        elif (userInput == 'Lower' or userInput == 'lower'):
            return False

# Would like this to have drawer draw a card and return current card
    def getCurrentCard(self):
        Drawer.getCurrentCard
