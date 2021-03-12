import arcade
from game import constants

class GameScreen(arcade.Window):
    """A lot like the arcade_batter's batter class. Inherits from arcade.window and runs the game.

    Attrs:
        song: a song that arcade can play
        cast: dictionary of sprites to display on screen
        script: dictionary of actions to execute
        input_service: the thing that lets us know what the user is doing.
    """
    def __init__(self, song, cast, script, input_service):
        """Initialize the game
        """
        super().__init__(constants.MAX_X, constants.MAX_Y, "The Drop")

        self._song = song
        self._cast = cast
        self._script = script
        self._input_service = input_service

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)

    def run(self):
        arcade.play_sound(self._song)
        super().run()

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

    def _cue_action(self, tag, *args):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
            *args (something): contains all the other arguments sent to this function.
        """ 
        for action in self._script[tag]:
            # if the code breaks here, add an if statement that checks
            # whether *args is None. If it is, then call action.execute
            # without *args.
            action.execute(self._cast, *args)