import arcade
from game import constants


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
