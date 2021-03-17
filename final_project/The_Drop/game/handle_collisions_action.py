import random
from game import constants
from game.action import Action


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
        beat = cast["beat"]

        for drop_point in drop_points:
            if drop_point.get_position().equals(beat.get_position()):
                beat.kill()
                # add points, not really sure how to do that from here
                return
            else:
                # subtract points, not really sure how to do taht from here
                # return

                # Just here for reference.
                return

    def _handle_beat_collision(self, beat, drop_points):
        actor_to_remove = None

        for point in drop_points:
            # This makes use of the `Sprite` functionality
            if beat.collides_with_sprite(point):
                beat.kill()
                actor_to_remove = beat

        if actor_to_remove != None:
            drop_points.remove(actor_to_remove)

    # could be super useful for if the beats were missed.
    def _is_off_screen(self, beat):
        # If the beat gets off the screen, it was missed.
        # We'll need to subtract some points, but not here.
        return beat.center_y < 0
