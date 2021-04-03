import arcade.gui
from arcade.gui.ui_style import UIStyle

class ChangeViewButton(arcade.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """

    def __init__(self, display, current_view, next_view, center_x, center_y, width=250, height=40, color=arcade.color.BLACK):
        """ display is the text for the button to show,
            current_view is a reference to the view creating this button,
            next_view is a string denoting which view this button should display next.
        """
        #style = UIStyle({})
        super().__init__(display, center_x, center_y, width, height)
        self.set_style_attrs(bg_color = color)
        self._view = current_view
        self._next_view = next_view
        self._has_prep = False

    def on_click(self):
        """ Called when user lets off button """
        if self._has_prep:
            self._prep_function(self)

        self._view._ui_manager.purge_ui_elements()
        if self._next_view == "menu":
            self._view.window.show_view(self._view.window.menu_view)
        if self._next_view == "instructions":
            self._view.window.show_view(self._view.window.instruction_view)
        if self._next_view == "game":
            self._view.window.show_view(self._view.window.game_screen)
        if self._next_view == "end":
            self._view.window.show_view(self._view.window.game_over_view)

    def set_prep_function(self, function):
        """ add a function to perform before showing the next view, like making the game screen.

        def the_prep_function(button, #params):
            #do stuff. 
        my_change_view_button.set_prep_function(the_prep_function)

        Note, define the_prep_function out of all classes so that button in this function will
        refer to the button. Or define it in a class and add a self parameter before button so
        you can reference the container class as well as the individual button.
        """

        self._has_prep = True
        self._prep_function = function