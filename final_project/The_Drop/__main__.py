from game import constants
from game.menu_view import MenuView
from game.instruction_view import InstructionView

# Add this back in when we're dealing with saving scores.
#from game.score_handler import ScoreHandler
import arcade


def main():

    # start the game
    window = arcade.Window(constants.MAX_X, constants.MAX_Y,"The Drop")
    window.menu_view = MenuView()
    window.instruction_view = InstructionView()
    window.show_view(window.menu_view)
    arcade.run()

if __name__ == "__main__":
    main()
