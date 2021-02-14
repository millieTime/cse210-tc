class Guess:
    def __init__(self):
        self.player_guess = 0
    
    def Get_guess(self,player_input):
        self.player_guess = player_input
        return self.player_guess