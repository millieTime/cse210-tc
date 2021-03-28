from game import constants
from game.menu_view import MenuView

# Add this back in when we're dealing with saving scores.
#from game.score_handler import ScoreHandler
import arcade


def main():

    # start the game
    window = arcade.Window(constants.MAX_X, constants.MAX_Y,"The Drop")
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()
