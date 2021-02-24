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
        ball = cast["ball"][0]
        bricks = cast["brick"]
        # loop through the bricks to bounce the ball off of and delete the brick
        for brick in bricks:
            if brick.get_position().equals(ball.get_position()):
                bricks.remove(brick)
                ball.reverse()                

        # check the paddle to see if the ball bounces off 
        # check the walls
        ball_velocity = ball.get_velocity()
        bounce_velocity = ball.get_velocity().reverse()
        if constants.MAX_X - 1 < ball.get_position.get_x < 1:
            ball.set_velocity(Point(bounce_velocity.get_x(), ball_velocity.get_y())
        elif ball.get_position.get_y < 1:
            ball.set_velocity(Point(ball_velocity.get_x, bounce_velocity.get_y())
        # check if the game is over (hits the ground)