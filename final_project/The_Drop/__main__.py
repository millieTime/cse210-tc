import random
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
from game.drop_point import DropBar
from game.game_screen import GameScreen

from game.score_handler import ScoreHandler
import arcade


def main():

    # create the cast {key: tag, value: list}
    cast = {}

    beat_map = BeatMap("memory")
    cast["beat_map"] = [beat_map]

    cast["beats"] = BeatMap.get_beats()

    keys = ['q', 'w', 'e', 'r']
    cast['drop_points'] = []
    for key in keys:
        cast['drop_points'].append(DropBar(key))

    song = arcade.load_sound(constants.PATH + "/assets/Coming_For_You/Coming_For_You.wav")

    # create the script {key: tag, value: list}
    script = {}

    input_service = Input(keys)
    output_service = Output()
    
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["move"] = [move_actors_action]
    script["collisions"] [handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    game_screen = GameScreen(song, cast, script, input_service)
    game_screen.setup()
    game_screen.run()