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
        self.score = 0
        self.drawer = Drawer()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            # do logic
            pass

    def getUserInput(self):
        userInput = input("Higher or Lower?: ")
        if (userInput == 'Higher' or userInput == 'higher'):
            return True
        elif (userInput == 'Lower' or userInput == 'lower'):
            return False

    def getCurrentCard(self):
        Drawer.getCurrentCard
    
    def update_points(self):
        if self.guess == True:
            if self.drawer.current > self.drawer.previous:
                self.score += 100
            else:
                self.score -= 75
        if self.guess == False:
            if self.drawer.current < self.drawer.previous_card:
                self.score += 100
            else:
                self.score -= 75
    
    def user_play_again(self):
        leave_loop = False
        while not leave_loop:   
            userplay = input('would you like to play again? (yes/no) > ').lower()
            if userplay == "yes":
                return True
            elif userplay == "no":
                return False
            else:
                Print('please choose yes or no.')