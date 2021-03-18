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

        drop_points = cast["drop_points"]

        beats = cast["beats"]

        player = cast["player"][0]

        # Check if there are beats that need to be removed.
        for beat in beats:
            if self._is_off_screen(beat):
                # will be zero if the beat has been scored. Otherwise,
                # the player needs to lose some points!
                points = beat.kill_and_points()
                player.subtract_points(points)
                beats.remove(beat)

        # Next, go through the drop_points and see whether they're scoring
        # or losing points.
        for drop_point in drop_points:
            # if the key is pressed,
            if drop_point.active():
                # check for collisions.
                self._handle_beat_collision(beats, drop_point, player)

    def _handle_beat_collision(self, beats, drop_point, player):
        #Whether the drop_point has hit a beat.
        has_collided = False

        for beat in beats:
            #if     they're in the same column,       and       they're close to overlapping
            if beat.get_key() == drop_point.get_key() and abs(beat.bottom - drop_point.bottom) < 20:
                has_collided = True
                # Can't double-score points because the beat's points get set to
                # zero after being scored =)
                points = beat.kill_and_points()
                player.add_points(points)
        # if the drop_point was hit at the wrong time,
        if not has_collided:
            player.subtract_points()
            

    # could be super useful for if the beats were missed.
    def _is_off_screen(self, beat):
        return beat.center_y + beat.height < 0
