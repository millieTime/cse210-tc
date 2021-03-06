
from game.Mastermind import Mastermind
from game.Console import Console
from game.Guess import Guess
from game.Player import Player
from game.Roster import Roster


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller
    Attributes:
        mastermind (Mastermind): An instance of the class of objects known as Mastermind.
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        roster (Roster): An instance of the class of objects known as Roster.
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        self._mastermind = Mastermind()
        self._console = Console()
        self._keep_playing = True
        self._roster = Roster()

    def start_game(self):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.

        Args:
            self (Director): An instance of Director.
        """
        for x in range(2):
            name = self._console.read(f"Enter a name for player {x + 1}: ")
            player = Player(name)
            self._roster.add_player(player)
            self._mastermind.prepare(player)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the guess from the current player.
        Args:
            self (Director): An instance of Director.
        """
        # display the mastermind info
        mastermind = self._mastermind.to_string()
        self._console.write(mastermind)
        # get next player's guess
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        player_response = self._console.read("What is your guess? ")
        guess = Guess(player_response)
        player.set_guess(guess)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the mastermind with the current guess.
        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current()
        guess = player.get_guess()
        self._mastermind.make_guess(player, guess)

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there is a winner and changing turns.
        Args:
            self (Director): An instance of Director.
        """
        if self._mastermind.has_won(self._roster.get_current()):
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._keep_playing = False
        self._roster.next_player()
