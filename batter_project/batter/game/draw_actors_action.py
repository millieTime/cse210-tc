from game.action import Action

class DrawActorsAction(Action):
    def __init__(self, output_service):
        self._output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actors(cast["bricks"])
        self._output_service.draw_actors(cast["paddle"])
        self._output_service.draw_actors(cast["ball"])
        self._output_service.flush_buffer()