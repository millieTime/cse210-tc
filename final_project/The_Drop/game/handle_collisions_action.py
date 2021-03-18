import random
from game import constants
from game.action import Action
from game.score import Score


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.

    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        # Yeah, this whole thing needs done.
        # for drop_point in cast["drop_points"]:
        #     if drop_point intersects with a beat:
        #         remove the beat, add some points
        #     if it didn't intersect with any:
        #         subtract some points

        drop_points = cast["drop_points"]
        beats = cast["beats"]
        player = cast["player"]

        for drop_point in drop_points:
            if drop_point.active():
                self._handle_beat_collision(beats, drop_point, player)

    def _handle_beat_collision(self, beats, drop_point, player):
        beat_to_remove = []
        has_collided = False

        for beat in beats:
            # This makes use of the `Sprite` functionality
            if beat.collides_with_sprite(drop_point):
                has_collided = True
                beat.kill()
                player.add_points()
                beat_to_remove.append(beat)

        if not has_collided:
            player.subtract_points()

        for beat in beat_to_remove:
            beats.remove(beat)

    # could be super useful for if the beats were missed.
    def _is_off_screen(self, beat):
        # If the beat gets off the screen, it was missed.
        # We'll need to subtract some points, but not here.
        return beat.center_y < 0
