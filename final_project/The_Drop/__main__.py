import random, time
from game import constants
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input import Input
from game.output import Output

from game.beat import Beat
from game.beat_map import BeatMap
from game.player import Player
from game.drop_point import DropPoint
from game.countdown import Countdown
from game.game_screen import GameScreen
from game.library import Library
from game.menu_view import MenuView

# Add this back in when we're dealing with saving scores.
#from game.score_handler import ScoreHandler
import arcade


def main():

    # start the game
    window = arcade.Window(constants.MAX_X, constants.MAX_Y,"The Drop")
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()
    


if __name__ == "__main__":
    main()
