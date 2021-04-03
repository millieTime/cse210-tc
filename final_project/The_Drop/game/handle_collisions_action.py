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

        all_beats = cast["beats"]
        relevant_beats = all_beats[-20:]

        player = cast["player"][0]

        # Check if there are beats that need to be removed.
        for beat in relevant_beats:
            if self._is_off_screen(beat):
                beat.kill_and_points()
                all_beats.remove(beat)

        # Next, go through the drop_points and see whether they're scoring
        # or losing points.
        for drop_point in drop_points:
            # if the key is pressed,
            if drop_point.active():
                # check for collisions.
                #reverse so it checks the lowest beats first
                self._handle_beat_collision(relevant_beats, drop_point, player)

    def _handle_beat_collision(self, beats, drop_point, player):
        #Whether the drop_point has hit a beat.
        has_collided = False

        for index in range(len(beats) -1, -1, -1):
            beat = beats[index]
            #if     they're in the same column,       and       they're close to overlapping
            if beat.get_key() == drop_point.get_key() and abs(beat.bottom - drop_point.bottom) < 30:
                has_collided = True
                # Can't double-score points because the beat's points get set to
                # zero after being scored =)
                points = beats[index].kill_and_points()
                player.add_points(points)
                # only allowed to score one beat at a time.
                break
        # if the drop_point was hit at the wrong time,
        if not has_collided:
            player.subtract_points(2)
            

    # could be super useful for if the beats were missed.
    def _is_off_screen(self, beat):
        return beat.center_y + beat.height < 0
