from game.action import Action

class DrawActorsAction(Action):
    #script["output"] is me
    #cast["artifact"] = artifacts. A list of artifacts.
    #cast["robot"] = [robot]. The robot
    #cast["marquee"] = [marquee]. The description
    def __init__(self, output_service):
        self._output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actors(cast["artifact"])
        self._output_service.draw_actors(cast["robot"])
        self._output_service.draw_actors(cast["marquee"])
        self._output_service.flush_buffer()