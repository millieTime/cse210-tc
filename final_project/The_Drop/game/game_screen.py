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

    def _cue_action(self, tag, delta_time = None):
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