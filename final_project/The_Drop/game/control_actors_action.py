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

    def __init__(self, input_service, keys):
        """The class constructor.

        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service
        self._keys = keys

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        # self._input_service is how we interact with the user. Whatever functions
        # implemented there will be useable here.
        for key in self._input_service.pressed_keys():
           cast['drop_points'][self._keys.index(key)].activate()
        for key in self._input_service.released_keys():
           cast['drop_points'][self._keys.index(key)].deactivate()

