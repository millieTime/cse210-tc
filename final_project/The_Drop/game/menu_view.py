import arcade
from game import constants
from game.library import Library


class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Draw the menu """
        '''
            display the songs, the songs will have a difficulty level next to it
        '''
        music_library = Library()

        arcade.start_render()

        arcade.draw_text("Menu Screen", constants.MAX_X/2, constants.MAX_Y/2 + 200,
                         arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text("What Level?", constants.MAX_X/2, constants.MAX_Y/2 + 125,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

        arcade.draw_text("Easy", constants.MAX_X/2, constants.MAX_Y/2 + 75,
                         arcade.color.WHITE, font_size=14, anchor_x="center")
        arcade.draw_text("Medium", constants.MAX_X/2, constants.MAX_Y/2 + 50,
                         arcade.color.WHITE, font_size=14, anchor_x="center")
        arcade.draw_text("Hard", constants.MAX_X/2, constants.MAX_Y/2 + 25,
                         arcade.color.WHITE, font_size=14, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view. """
        if _y == constants.MAX_Y / 2 + 75:
            # easy
            pass
        elif _y == constants.MAX_Y / 2 + 50:
            # medium
            pass
        elif _y == contants.MAX_Y / 2 + 25:
            # hard
            pass
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)

    '''
    on_mouse_release(x: float, y: float, button: int, modifiers: int)[source]
        Override this function to add mouse button functionality.

        Parameters
        x (float) –

        y (float) –

        button (int) –

        modifiers (int) – Bitwise ‘and’ of all modifiers (shift, ctrl, num lock) pressed during this event. See Modifiers.
    '''
