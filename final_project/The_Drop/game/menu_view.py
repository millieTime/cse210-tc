import arcade
from game import constants
from game.game_screen import GameScreen
from game.library import Library
import arcade.gui
from arcade.gui import UIManager

# lib = Library()
# names = lib.get_song_names()
# print("Song names: ")
#  print(names)
#   song = ""
#    while not song in names:
#         song = input("Which song to play? ")
#     song_info = lib.get_song(song)
#     levels = song_info.get_level_names()
#     print("levels: ")
#     print(levels)
#     level = 0
#     while not level in levels:
#         level = input("Which level to play? ")
#     level = levels.index(level)


class MyFlatButton(arcade.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """

    def __init__(self, song, view, uimanager, center_x, center_y, width, height=20):
        super().__init__(song, center_x, center_y, width, height)
        self.ui_manager = uimanager
        self._song = song
        self._menu_view = view

    def on_click(self):
        """ Called when user lets off button """
        song_obj = self._menu_view._lib.get_song(self._song)
        self.ui_manager.purge_ui_elements()
        game_screen = GameScreen(song_obj)
        self._menu_view.window.show_view(game_screen)


class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """

    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()
        self._lib = Library()

    def on_show(self):
        """ Called when switching to this view"""

        arcade.set_background_color(arcade.color.BLACK)
        self._names = self._lib.get_song_names()
        self.setup()

    def setup(self):
        self.ui_manager.purge_ui_elements()
        counter = 125
        for songName in self._names:
            button = MyFlatButton(
                songName,
                self,
                self.ui_manager,
                center_x=constants.MAX_X/2,
                center_y=constants.MAX_Y/2 + counter,
                width=250,
            )
            self.ui_manager.add_ui_element(button)
            counter -= 25

    def on_draw(self):
        """ Draw the menu """
        '''
            display the songs, the songs will have a difficulty level next to it
        '''
        arcade.start_render()
        arcade.draw_text("Menu Screen", constants.MAX_X/2, constants.MAX_Y/2 + 200,
                         arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text("Song Names", constants.MAX_X/2, constants.MAX_Y/2 + 170,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
