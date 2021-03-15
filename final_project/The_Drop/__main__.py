# import random
# from game import constants
# from game.point import Point
# from game.control_actors_action import ControlActorsAction
# from game.draw_actors_action import DrawActorsAction
# from game.handle_collisions_action import HandleCollisionsAction
# from game.move_actors_action import MoveActorsAction
# from game.input import Input
# from game.output import Output

# from game.beat import Beat
# from game.beat_map import Beat_Map
# from game.player import Player
# from game.drop_point import Drop_Point
# from game.game_screen import GameScreen

# #from game.score_handler import ScoreHandler
# import arcade


# def main():

#     # create the cast {key: tag, value: list}
#     cast = {}

#     beat_map = Beat_Map()
#     cast["beat_map"] = [beat_map]

#     cast["beats"] = beat_map.get_beats()

#     keys = ['q', 'w', 'e', 'r']
#     cast['drop_points'] = []
#     for key in keys:
#         cast['drop_points'].append(Drop_Point(key))

#     song = arcade.load_sound("C:/Users/Jesat/Desktop/College/BYUI/Winter2021/CSE210/cse210-tc/final_project/The_Drop/assets/songs/Neo/neo.mp3")

#     # create the script {key: tag, value: list}
#     script = {}

#     input_service = Input()
#     output_service = Output()
    
#     control_actors_action = ControlActorsAction(input_service)
#     move_actors_action = MoveActorsAction()
#     handle_collisions_action = HandleCollisionsAction()
#     draw_actors_action = DrawActorsAction(output_service)
    
#     script["input"] = [control_actors_action]
#     script["move"] = [move_actors_action]
#     #script["collisions"] [handle_collisions_action]
#     script["output"] = [draw_actors_action]

#     # start the game
#     game_screen = GameScreen(song, cast, script, input_service)
#     game_screen.setup()
#     game_screen.run()


# main()

# Imports
import arcade
import random
import os

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
beat_test = {
    # 1st section
    "1" : (SCREEN_WIDTH / 4 * 1),
    # 2nd section
    "2" : (SCREEN_WIDTH / 4 * 2), 
    # 3rd section
    "3" : (SCREEN_WIDTH / 4 * 3), 
    # 4th section
    "4" : (SCREEN_WIDTH / 4 * 4), 
}
SCREEN_TITLE = "The Drop"
PATH = os.path.dirname(os.path.abspath(__file__))
SCALING = 2.0


class FlyingSprite(arcade.Sprite):
    """Base class for all flying sprites
    Flying sprites include beats and clouds
    """

    def update(self):
        """Update the position of the sprite
        When it moves off screen to the left, remove it
        """

        # Move the sprite
        super().update()

        # Remove us if we're off screen
        if self.right < 0:
            self.remove_from_sprite_lists()

class game_screen(arcade.Window):

    def __init__(self, width: int, height: int, title: str):
        """Initialize the game"""
        super().__init__(width, height, title)

        # Setup the empty sprite lists
        self.beats_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

    def setup(self):
        """Get the game ready to play"""

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

        # Setup the player
        self.player = arcade.Sprite(PATH + "/assets/images/drop_point_deactivated.png", SCALING/2)
        self.player.left = beat_test["1"]
        self.player.center_y = SCREEN_HEIGHT / 4 
        self.all_sprites.append(self.player)
        

        # Spawn a new beat every second
        arcade.schedule(self.add_beat, 1)

        # Load background music
        self.background_music = arcade.load_sound(
            PATH + "/assets/songs/Neo/neo.mp3"
        )

        # Load our other PATH + "/sounds
        # Sound sources: Jon Fincher
        #self.collision_sound = arcade.load_sound(PATH + "/sounds/Collision.wav")
       
        # Start the background music
        arcade.play_sound(self.background_music)

        # Unpause everything and reset the collision timer
        self.paused = False
        self.collided = False
        self.collision_timer = 0.0
        

    def add_beat(self, delta_time: float):
        """Adds a new beat to the screen

        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """

        # First, create the new beat sprite
        beat = FlyingSprite(PATH + "/assets/images/beat_1.png", SCALING/2)

        # Set its position to a random height and off screen right
        pos = str(random.randint(1, 4))
        beat.left = beat_test[pos]
        beat.top = random.randint(self.height, self.height + 10)

        # Set its speed to a random speed heading left
        beat.velocity = (0, -100)

        # Add it to the beats list
        self.beats_list.append(beat)
        self.all_sprites.append(beat)

    def on_key_press(self, symbol: int, modifiers: int):
        """Handle user keyboard input
        Q: Quit the game
        P: Pause the game
        I/J/K/L: Move Up, Left, Down, Right
        Arrows: Move Up, Left, Down, Right

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if symbol == arcade.key.ESCAPE:
            # Quit immediately
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused

        if symbol == arcade.key.Q:
            self.player.left = beat_test["1"]

        if symbol == arcade.key.W:
            self.player.left = beat_test["2"]
        
        if symbol == arcade.key.E:
            self.player.left = beat_test["3"]
        
        if symbol == arcade.key.R:
            self.player.left = beat_test["4"]

        

    def on_key_release(self, symbol: int, modifiers: int):
        """Undo movement vectors when movement keys are released

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        # if (
        #     symbol == arcade.key.Q
        #     or symbol == arcade.key.W
        #     or symbol == arcade.key.E
        #     or symbol == arcade.key.R
        # ):
        #     self.player.right = -200
        pass


    def on_update(self, delta_time: float):
        """Update the positions and statuses of all game objects
        If we're paused, do nothing
        Once everything has moved, check for collisions between
        the player and the list of beats

        Arguments:
            delta_time {float} -- Time since the last update
        """

        # Did we collide with something earlier? If so, update our timer
        if self.collided:
            self.collision_timer += delta_time
            # If we've paused for two seconds, we can quit
            if self.collision_timer > 2.0:
                arcade.close_window()
            # Stop updating things as well
            return

        # If we're paused, don't update anything
        if self.paused:
            return

        print(self.collision_timer)
        if delta_time == 30:
            arcade.close_window()


        # Did we hit anything? If so, end the game
        # if self.player.collides_with_list(self.beats_list):
        #     self.collided = True
        #     self.collision_timer = 0.0
        #     arcade.play_sound(self.collision_sound)

        # Update everything
        for sprite in self.all_sprites:
            sprite.center_x = int(
                sprite.center_x + sprite.change_x * delta_time
            )
            sprite.center_y = int(
                sprite.center_y + sprite.change_y * delta_time
            )
        # self.all_sprites.update()

        

    
    def on_draw(self):
        """Draw all game objects"""

        arcade.start_render()
        self.all_sprites.draw()



if __name__ == "__main__":
    # Create a new Space Shooter window
    drop_game = game_screen(
        int(SCREEN_WIDTH * SCALING), int(SCREEN_HEIGHT * SCALING), SCREEN_TITLE
    )
    # Setup to play
    drop_game.setup()
    # Run the game
    arcade.run()