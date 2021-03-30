import arcade
from game import constants
from game.change_view_button import ChangeViewButton
from game.drop_point import DropPoint
from game.beat import Beat
from game.input import Input
from game.control_actors_action import ControlActorsAction
from arcade.gui import UIManager
from arcade.gui import ui_style
from arcade.gui import UIElement

class InstructionView(arcade.View):
    """ Class that manages the 'menu' view. """

    def __init__(self):
        super().__init__()
        
        self._ui_manager = UIManager()
        keys=['q', 'w', 'e', 'r']
        self._input = Input(keys)
        self._activator = ControlActorsAction(self._input, keys)
        
        with open(constants.DIRROOT + "/assets/text/instructions.txt") as infile:
            self._instruction_text = [x[:-1] for x in infile.readlines()]
        
        self._beats = []
        self._drop_points = []
        for key in keys:
            beat = Beat(key, 0.15)
            self._beats.append(beat)
            drop_point = DropPoint(key, 177)
            self._drop_points.append(drop_point)

    def on_show(self):
        """ Called when switching to this view"""

        arcade.set_background_color(arcade.color.BLACK)
        self.setup()

    def setup(self):
        self._ui_manager.purge_ui_elements()
        button = ChangeViewButton(
            "Back",
            self,
            "menu",
            center_x=constants.MAX_X - 110,
            center_y=30,
            width=100,
        )
        self._ui_manager.add_ui_element(button)

    def on_draw(self):
        """ Draw the menu """
        '''
            display the songs, the songs will have a difficulty level next to it
        '''

        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,constants.MAX_X,constants.MAX_Y,arcade.load_texture(constants.MAIN_MENU_IMAGE))
        arcade.draw_text("The", constants.MAX_X/2, constants.MAX_Y/2 + 325, 
                         arcade.color.WHITE, font_size=40, font_name='impact', anchor_x="right",anchor_y='top')
        arcade.draw_text("Drop", constants.MAX_X/2, constants.MAX_Y/2 + 325,
                         arcade.color.WHITE, font_size=70, font_name='impact', anchor_x="left",anchor_y='top')
        
        for index in range(len(self._drop_points)):
            self._drop_points[index].draw()
            self._beats[index].draw()
        counter = 200
        for line in self._instruction_text:
            if line:
                arcade.draw_rectangle_filled(constants.MAX_X/2, constants.MAX_Y /2 + counter - 2,
                                            constants.MAX_X - 50, 26, arcade.color.EERIE_BLACK)
                if line != " ":
                    arcade.draw_text(
                        line,
                        60, constants.MAX_Y / 2 + counter,
                        arcade.color.REDWOOD, font_size=16,
                        #width = constants.MAX_X - 100,
                        anchor_x= 'left', anchor_y="center"
                    )
                    # lower by 10 more bc it has text to surround
                    counter -= 10
            # always lower by 10
            counter -= 10

    def on_key_press(self, symbol, modifiers):
        # Adds a key to the list of keys currently pressed
        self._input.set_key(symbol, modifiers)
        self._activator.execute({"drop_points":self._drop_points})

    def on_key_release(self, symbol, modifiers):
        # Removes a key from the list of keys currently pressed
        self._input.remove_key(symbol, modifiers)
        self._activator.execute({"drop_points":self._drop_points})
