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
        #Yeah, this whole thing needs done.
        # for drop_point in cast["drop_points"]:
        #     if drop_point intersects with a beat:
        #         remove the beat, add some points
        #     if it didn't intersect with any:
        #         subtract some points
        return
        
    # Just here for reference.
    def _handle_brick_collision(self, ball, bricks):
        brick_to_remove = None

        for brick in bricks:
            # This makes use of the `Sprite` functionality
            if ball.collides_with_sprite(brick):
                ball.bounce_horizontal()
                brick_to_remove = brick

        if brick_to_remove != None:
            bricks.remove(brick_to_remove)

    #could be super useful for if the beats were missed.
    def _is_off_screen(self, beat):
        # If the beat gets off the screen, it was missed.
        # We'll need to subtract some points, but not here.
        return beat.center_y < 0
