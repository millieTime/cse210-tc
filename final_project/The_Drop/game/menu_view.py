import arcade
from game import constants
from game.game_screen import GameScreen
from game.library import Library
from game.change_view_button import ChangeViewButton
import arcade.gui
from arcade.gui import UIManager

class ChangeViewsButton(arcade.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """

    def __init__(self, song, input_box, view, uimanager, center_x, center_y, width=250, height=40):
        super().__init__(song, center_x, center_y, width, height)
        self._ui_manager = uimanager
        self._view = view
        self._song = song
        self._input_box = input_box

def _prep_game(self):
    """ for when the user clicks a button. """
    song_obj = self._view._lib.get_song(self._song)
    self._view.window.game_screen = GameScreen(song_obj, self._input_box.text)

class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """

    def __init__(self):
        super().__init__()
        self._ui_manager = UIManager()
        self._lib = Library()

    def on_show(self):
        """ Called when switching to this view"""

        arcade.set_background_color(arcade.color.BLACK)
        self._names = self._lib.get_song_names()
        self.setup()

    def setup(self):
        self._ui_manager.purge_ui_elements()

        self._ui_input_box = arcade.gui.UIInputBox(
            center_x=constants.MAX_X/2,
            center_y=constants.MAX_Y/2 + 100,
            width=300
        )
        self._ui_input_box.text = ''
        self._ui_input_box.cursor_index = len(self._ui_input_box.text)
        self._ui_manager.add_ui_element(self._ui_input_box)

        counter = 0
        for songName in self._names:
            button = ChangeViewButton(
                songName,
                self,
                "game",
                center_x=constants.MAX_X/2,
                center_y=constants.MAX_Y/2 + counter,
            )
            button._song = songName
            button._input_box = self._ui_input_box
            button.set_prep_function(_prep_game)
            self._ui_manager.add_ui_element(button)
            counter -= 50

        instruction_button = ChangeViewButton(
            "Instructions",
            self,
            "instructions",
            constants.MAX_X - 220,
            25,
            200,
            50
        )
        self._ui_manager.add_ui_element(instruction_button)

    def on_draw(self):
        """ Draw the menu """
        '''
            display the songs, the songs will have a difficulty level next to it
        '''

        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,constants.MAX_X,constants.MAX_Y,arcade.load_texture(constants.MAIN_MENU_IMAGE))
        arcade.draw_rectangle_filled(constants.MAX_X / 2, constants.MAX_Y / 2 + 38, 175, 35, arcade.color.EERIE_BLACK)
        arcade.draw_text("The", constants.MAX_X/2, constants.MAX_Y/2 + 250, 
                         arcade.color.WHITE, font_size=40, font_name='impact', anchor_x="right",anchor_y='top')
        arcade.draw_text("Drop", constants.MAX_X/2, constants.MAX_Y/2 + 250,
                         arcade.color.WHITE, font_size=70, font_name='impact', anchor_x="left",anchor_y='top')
        arcade.draw_text("Input Your Name", constants.MAX_X/2, constants.MAX_Y/2 + 125,
                         arcade.color.WHITE, font_size=16, anchor_x="center")
        arcade.draw_text("--Song Names--", constants.MAX_X/2, constants.MAX_Y/2 + 25,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
