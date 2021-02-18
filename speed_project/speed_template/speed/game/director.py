from time import sleep
from game import constants
from game.score import Score
from game.game_word import Game_word
from game.user_input import User_input

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        user_input (User_input): What the user inputs into the console
        game_word (Game_word): Handle each word being used within the game
        word_list (List): A list that contains the 5 words being used in the game
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._user_input = User_input()
        self._game_word = Game_word()
        self._word_list = []
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the most recent typed letters and moving the words.

        Args:
            self (Director): An instance of Director.
        """
        
        self._user_input.set_input_word(self._input_service.get_letter())
        

        pass

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking if a word made it to the wall, and
        updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self._check_word_position()
        self._check_user_input()
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        # Later, we will write out the words in this spot
        ## self._output_service.draw_actor(self._food)
        ## self._output_service.draw_actors(self._snake.get_all())
        ## self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()

    def _check_word_position(self):
        #go through the list of game words and see if any made it to the edge of the screen.
        pass

    def _check_user_input(self):
        #this method is only called if the most recent input from the input_servic was a *
        # in that case, check if the user's word matches anything in our word list
        pass