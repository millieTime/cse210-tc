from game.action import Action
from game import constants

import arcade


class DrawActorsAction(Action):
    """A code template for drawing actors.

    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service):
        """The class constructor.

        Args:
            _output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()

        

        beats = cast["beats"]
        beats = beats[-20:]
        for beat in beats:
            self._output_service.draw_actor(beat)

        players = cast["player"]
        for player in players:
            self._output_service.draw_actor(player)
            
        for drop_point in cast["drop_points"]:
            self._output_service.draw_actor(drop_point)

        self._output_service.flush_buffer()
