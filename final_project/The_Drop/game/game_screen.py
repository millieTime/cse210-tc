import arcade
from game import constants
from game.beat_map import BeatMap
from game.player import Player
from game.drop_point import DropPoint
from game.input import Input
from game.output import Output
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction


class GameScreen(arcade.View):
    """A lot like the arcade_batter's batter class. Inherits from arcade.window and runs the game.

    Attrs:
        song: a song that arcade can play
        cast: dictionary of sprites to display on screen
        script: dictionary of actions to execute
        input_service: the thing that lets us know what the user is doing.
    """

    def __init__(self, song, player_name):
        """Initialize the game
        """
        super().__init__()
        self._song_object = song

        beat_map = BeatMap()
        beat_map.read_file(self._song_object.get_level_file(0))

        # create the cast {key: tag, value: list}
        cast = {}
        cast["beats"] = beat_map.get_beats()
        cast["beats"].reverse()

        keys = ['q', 'w', 'e', 'r']
        cast['drop_points'] = []
        for key in keys:
            cast['drop_points'].append(DropPoint(key))

        player = Player(player_name, keys)
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

        self._song = arcade.Sound(self._song_object.get_song(), streaming=True)
        self._cast = cast
        self._script = script
        self._input_service = input_service

    def on_show(self):
        self.setup()

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)
        # returns a pyglet media player object that we can use to control what happens when the song ends!
        self._media_player = self._song.play()

        def on_eos():
            arcade.close_window()

        self._media_player.push_handlers(on_eos)

    def on_update(self, delta_time):
        # delta_time: the time between frames. used to calculate sprite exact speed.
        self._cue_action("move", delta_time)
        self._cue_action("collisions")

    def on_draw(self):
        self._cue_action("output")

    def on_key_press(self, symbol, modifiers):
        # Adds a key to the list of keys currently pressed
        self._input_service.set_key(symbol, modifiers)
        self._cue_action("input")

    def on_key_release(self, symbol, modifiers):
        # Removes a key from the list of keys currently pressed
        self._input_service.remove_key(symbol, modifiers)
        self._cue_action("input")

    def _cue_action(self, tag, delta_time=None):
        """Executes the actions with the given tag.

        Args:
            tag (string): The given tag.
            delta_time (number): how long it has been since on_draw was last called.
        """
        for action in self._script[tag]:
            if (delta_time):
                action.execute(self._cast, delta_time)
            else:
                action.execute(self._cast)
