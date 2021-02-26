import random
from game import constants
from game.action import Action
from game.point import Point


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
        paddle = cast["paddle"][0]
        bricks = cast["bricks"]

        # loop through the bricks to bounce the ball off of and delete the brick
        for brick in bricks:
            if brick.get_position().equals(ball.get_position()):
                bricks.remove(brick)
                ball.set_velocity(ball.get_velocity().bounce_y())
        if not bricks:
            return +1

        # check the paddle to see if the ball bounces off
        # check the walls
        if ball.get_position().get_x() >= constants.MAX_X - 2 or ball.get_position().get_x() <= 2:
            ball.set_velocity(ball.get_velocity().bounce_x())
        if ball.get_position().get_y() <= 1:
            ball.set_velocity(ball.get_velocity().bounce_y())
        elif ball.get_position().get_y() == constants.MAX_Y - 2:
            if paddle.get_position().get_x() < ball.get_position().get_x() and ball.get_position().get_x() < paddle.get_position().get_x() + len(paddle.get_text()):
                if ball.get_position().get_x() < paddle.get_position().get_x() + (len(paddle.get_text())/2):
                    ball.set_velocity(ball.get_velocity().bounce_left())
                else:
                    ball.set_velocity(ball.get_velocity().bounce_right())
                ball.set_velocity(ball.get_velocity().bounce_y())
            else:
                return -1
