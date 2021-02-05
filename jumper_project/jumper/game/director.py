from game.parachute import Parachute
from game.Console import Console
from game.wordhandler import WordHandler


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.

    Attributes:
        parachute (Parachute): an instance of the class Parachute.
        keep_playing (boolean): Whether or not the game can continue.
        console (Console): an instance of the class Console.
        wordhandler (WordHandler): an instance of the class WordHandler.
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        self.parachute = Parachute()
        self.console = Console()
        self.keep_playing = True
        self.wordhandler = WordHandler()

    def start_game(self):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """
        self.do_outputs()
        while self.keep_playing:
            self.get_inputs()
            self.do_outputs()
        
        self.game_over()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means asking the user for a letter.

        Args:
            self (Director): An instance of Director.
        """
        userInput = self.console.read_letter("Guess a letter [a-z]: ")
        while not self.wordhandler.canBeGuessed(userInput):
            self.console.write("You already guessed that letter")
            userInput = self.console.read_letter("Guess a letter [a-z]: ")
        if not self.wordhandler.checkLetter(userInput):
            self.parachute.guessed_wrong()

    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means showing the guessed letters and parachuter.

        Args:
            self (Director): An instance of Director.
        """
        self.console.write(self.wordhandler.word_display())
        self.console.write(self.parachute.get_art())
        self.keep_playing = not (self.parachute.is_dead() or self.wordhandler.wordFound())

    def game_over(self):
        """Outputs some friendly text depending on how the game ends

        Args:
            self (Director): An instance of Director.
        """
        if self.parachute.is_dead():
            self.console.write("Aww, Game Over!")
        else:
            self.console.write("Nice job! You got it!")
