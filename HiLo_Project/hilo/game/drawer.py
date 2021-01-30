from random import seed
from random import randint

class Drawer:
    def __init__(self):
        self.current = 0
        self.previous = 0

    def draw_new_card(self):
        self.previous = self.current
        while True:
            self.current = randint(1, 13)
            if self.current != self.previous:
                break
        
        
    # def current(self):
        # return self.current

    # def previous(self):
    #     return self.previous
