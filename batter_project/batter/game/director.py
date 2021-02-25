from time import sleep
from game import constants

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script
        self._game_is_over = False
        
    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        while not self._game_is_over:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")
            sleep(constants.FRAME_LENGTH)
        if self._game_is_over == 1:
            print('Today\'s forcast: 100 percent chance of winning!')
        else:
            print('Sorry, you lost! "Tis but a flesh wound!!"')


    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            return_value = action.execute(self._cast)
            if return_value:
                self._game_is_over = return_value