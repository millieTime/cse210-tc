import arcade
from game import constants

class Countdown(arcade.Sprite):
    # want this to show 3, 2, 1, so I'll need to override update and increment some timer to keep track of the number here.
    # Won't have pictures so much as it will have text that starts big and gets small.
    def __init__(self, song):
        #song: a song that arcade can play
        # add 3, 2, 1 images
        super().__init__(constants.CDIMAGE_3)
        self.append_texture(arcade.load_texture(constants.CDIMAGE_2))
        self.append_texture(arcade.load_texture(constants.CDIMAGE_1))
        self._stage = -1
        self._time = 0
        self.change_x = 1
        self._center_x = constants.MAX_X / 2
        self.center_y = constants.MAX_Y / 2

        self._song = song
    
    @property
    def center_x(self):
        return self._center_x
	
    @center_x.setter
    def center_x(self, new_x):
        self.increment_timer(new_x - constants.MAX_X / 2)

    def draw(self):
        if self._stage < 3:
            super().draw()
    
    def increment_timer(self, elapsed):
        self._time += elapsed 
        if self._time // 1 > self._stage:
            # 1 whole second has elapsed.
            self._stage = int(self._time // 1)
            # If this is the very first call, ignore elapsed time.
            # It couses audio sync issues.
            if self._stage == 0:
                self._time = 0
            # 2-3rd? change image.
            elif self._stage < 3:
                self.set_texture(self._stage)
            # 4th? Start the music and lets go!
            elif self._stage == 3:
                # returns a pyglet media player object that we can use to control what happens when the song ends!
                self._media_player = self._song.play()
                def on_eos():
                    arcade.close_window()
                self._media_player.push_handlers(on_eos)
        

