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
        self._word_list = []
        for _ in range(5):
            self._word_list.append(Game_word())
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        loop_count = 0
        while self._keep_playing:
            self._get_inputs(loop_count == 0)
            self._do_updates()
            self._do_outputs()
            loop_count = (loop_count + 1) % 5
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self, move_words):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the most recent typed letters and moving the words.

        Args:
            self (Director): An instance of Director.
        """
        self._user_input.set_input_word(self._input_service.get_letter())
        if (move_words):
            for word in self._word_list:
                word.move_next()

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
        self._output_service.draw_actor(self._user_input)
        self._output_service.draw_actors(self._word_list)
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()

    def _check_word_position(self):
        #go through the list of game words and see if any made it to the edge of the screen.
        for word in self._word_list:
            if word.get_position().get_x() >= constants.MAX_X - 5:
                self._keep_playing = False
                print("You Lose!")
                break

    def _check_user_input(self):
        #check if the user's word matches anything in our word list
        user_word = self._user_input.get_input_word()
        if user_word and user_word[-1] == "*":
            for word in self._word_list:
                if word.get_text() == user_word[:-1]:
                    self._score.add_points(word.get_points())
                    word.reset()
                    break
            self._user_input.clear()