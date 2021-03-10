import random
from game import constants
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.arcade_input_service import ArcadeInputService
from game.arcade_output_service import ArcadeOutputService

from game.beat import Beat
from game.beat_map import BeatMap
from game.player import Player

from game.score_handler import ScoreHandler
import arcade


def main():

    # create the cast {key: tag, value: list}
    cast = {}

    beat_map = BeatMap("memory")
    cast["beat_map"] = [beat_map]

    cast["beats"] = BeatMap.get_beats()

    ### We'll need to figure out audio. These lines were copied in from another file
        self.collision_sound = arcade.load_sound(PATH + "/sounds/Collision.wav")
    arcade.play_sound(self.background_music)

    ##############################
    #Below this line is only copied from arcade_batter's main
    ##############################

    # create the script {key: tag, value: list}
    script = {}

    input_service = ArcadeInputService()
    output_service = ArcadeOutputService()
    
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    batter = Batter(cast, script, input_service)
    batter.setup()
    arcade.run()