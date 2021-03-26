import arcade
from game import constants

class Countdown(arcade.Sprite):
    # want this to show 3, 2, 1, so I'll need to override update and increment some timer to keep track of the number here.
    # Won't have pictures so much as it will have text that starts big and gets small.
    def __init__(self, song):
        #song: a song that arcade can play
        # add number images
        super().__init__()
        for image in constants.CDIMAGES:
            self.append_texture(arcade.load_texture(image))
        self.set_texture(constants.COUNTDOWN - 1)
        self._stage = -1
        self._time = 0
        self.change_x = 1
        self._center_x = constants.MAX_X / 2
        self.center_y = constants.MAX_Y / 2

        self._song = song
        self._media_player = self._song.play()
        self._song.stop(self._media_player)
        self._media_player.seek(0)
        def on_player_eos():
            arcade.close_window()
        self._media_player.on_player_eos = on_player_eos
    
    @property
    def center_x(self):
        return self._center_x
	
    @center_x.setter
    def center_x(self, new_x):
        #pass
        self.increment_timer(new_x - constants.MAX_X / 2)

    def draw(self):
        if self._stage < constants.COUNTDOWN:
            super().draw()
    
    def increment_timer(self, elapsed):
        self._time += elapsed 
        if self._time // 1 > self._stage:
            # 1 whole second has elapsed.
            self._stage = int(self._time // 1)
            # Change image to next number.
            if self._stage < constants.COUNTDOWN:
                self.set_texture(self._stage)
            # Start the music and lets go!
            elif self._stage == constants.COUNTDOWN:
                self._media_player.play()
        

