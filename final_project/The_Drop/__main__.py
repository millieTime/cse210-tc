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
from game.drop_point import DropPoint
from game.game_screen import GameScreen

# Add this back in when we're dealing with saving scores.
#from game.score_handler import ScoreHandler
import arcade


def main():

    # create the cast {key: tag, value: list}
    cast = {}
    song = arcade.Sound(
        constants.DIRROOT + "/assets/songs/Mayday/Mayday.mp3")
    

    beat_map = BeatMap()
    beat_map.read_file(constants.DIRROOT + "/assets/songs/Mayday/Mayday_1.txt")

    cast["beats"] = beat_map.get_beats()

    keys = ['q', 'w', 'e', 'r']
    cast['drop_points'] = []
    for key in keys:
        cast['drop_points'].append(DropPoint(key))

    player = Player('Random', keys)
    cast['player'] = [player]

    # create the script {key: tag, value: list}
    script = {}

    input_service = Input(keys)
    output_service = Output()

    control_actors_action = ControlActorsAction(input_service, keys)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)

    script["input"] = [control_actors_action]
    script["move"] = [move_actors_action]
    script["collisions"] = [handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    game_screen = GameScreen(song, cast, script, input_service)
    game_screen.setup()
    arcade.run()


if __name__ == "__main__":
    main()
