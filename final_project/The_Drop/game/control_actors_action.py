from game import constants
from game.action import Action


class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.

    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.

        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        # self._input_service is how we interact with the user. Whatever functions
        # implemented there will be useable here.

        # If the player has a key pressed, we want to make some object interactable
        # in that column. In another class, we'll check if those objects are overlappiing
        # and award points if true, subtract points if false.
        cast['drop_bars'][key].activate

