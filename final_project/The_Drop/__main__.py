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
from game.countdown import Countdown
from game.game_screen import GameScreen
from game.library import Library
from game.menu_view import MenuView

# Add this back in when we're dealing with saving scores.
#from game.score_handler import ScoreHandler
import arcade


def main():


    # Figure out which song we're playing.
    lib = Library()
    names = lib.get_song_names()
    print("Song names: ")
    print(names)
    song = ""
    while not song in names:
        song = input("Which song to play? ")
    song_info = lib.get_song(song)
    levels = song_info.get_level_names()
    print("levels: ")
    print(levels)
    level = 0
    while not level in levels:
        level = input("Which level to play? ")
    level = levels.index(level)
    
    # read song files.
    song = arcade.Sound(song_info.get_song())
   
    beat_map = BeatMap()
    beat_map.read_file(song_info.get_level_file(level), constants.COUNTDOWN)

    # create the cast {key: tag, value: list}
    cast = {}
    cast["beats"] = beat_map.get_beats()
    cast["beats"].reverse()

    keys = ['q', 'w', 'e', 'r']
    cast['drop_points'] = []
    for key in keys:
        cast['drop_points'].append(DropPoint(key))

    player = Player('Random', keys)
    cast['player'] = [player]

    cast['countdown'] = [Countdown()]
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
    #window = arcade.Window(constants.MAX_X, constants.MAX_Y,
    #                       "Different Views Minimal Example")
    #menu_view = MenuView()
    #window.show_view(menu_view)
    game_screen = GameScreen(song, cast, script, input_service)
    game_screen.setup()
    arcade.run()


if __name__ == "__main__":
    main()
