import arcade
from game import constants
from game.change_view_button import ChangeViewButton
import arcade.gui
from arcade.gui import UIManager


class GameOverScreen(arcade.View):
    """ Class that manages the 'menu' view. """

    def __init__(self, player):
        super().__init__()
        self._player = player
        self._ui_manager = UIManager()

    def on_show(self):
        """ Called when switching to this view"""

        arcade.set_background_color(arcade.color.BLACK)
        self.setup()

    def setup(self):
        self._ui_manager.purge_ui_elements()

        button = ChangeViewButton(
            "Play Again!",
            self,
            "menu",
            center_x=constants.MAX_X/2,
            center_y=constants.MAX_Y/2 - 100,
        )
        self._ui_manager.add_ui_element(button)
        self._player_accuracy = self._player.get_accuracy()
        if self._player_accuracy == 1:
            self._player_rating = "<<<BEAT MASTER>>>"
        elif self._player_accuracy > .9:
            self._player_rating = "Beat Master"
        elif self._player_accuracy > .8:
            self._player_rating = "Beat Novice"
        elif self._player_accuracy > .7:
            self._player_rating = "Beat Tryhard"
        elif self._player_accuracy > 0:
            self._player_rating = "beat dropout"
        else:
            self._player_rating = ">>>The Anti-Beat<<<"

    def on_draw(self):
        """ Draw the menu """
        '''
            display the songs, the songs will have a difficulty level next to it
        '''

        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(
            0, 0, constants.MAX_X, constants.MAX_Y, arcade.load_texture(constants.MAIN_MENU_IMAGE))
        arcade.draw_text("The", constants.MAX_X/2, constants.MAX_Y/2 + 250,
                         arcade.color.WHITE, font_size=40, font_name='impact', anchor_x="right", anchor_y='top')
        arcade.draw_text("Drop", constants.MAX_X/2, constants.MAX_Y/2 + 250,
                         arcade.color.WHITE, font_size=70, font_name='impact', anchor_x="left", anchor_y='top')
        self.draw_rect_text("Your Score: ", constants.MAX_Y/2 + 90, 16)
        self.draw_rect_text(str(self._player), constants.MAX_Y/2 + 60, 20)
        self.draw_rect_text("Beat Master Rating: " + format(self._player_accuracy, '.1%'), constants.MAX_Y/2 + 10, 16)
        self.draw_rect_text(self._player_rating, constants.MAX_Y/2 - 25, 20)
    
    def draw_rect_text(self, text, y, font_size):
        arcade.draw_rectangle_filled(constants.MAX_X / 2, y + 13, len(text) * font_size * 4/5, 2 * font_size, arcade.color.EERIE_BLACK)
        arcade.draw_text(text, constants.MAX_X/2, y, arcade.color.WHITE, font_size=font_size, anchor_x="center")
