

class Parachute:

    def __init__(self):
        self.art = ["  ___",
                    " /___\\",
                    " \\   /",
                    "  \\ /",
                    "   0",
                    "  /|\\",
                    "  / \\",
                    "\n^^^^^^^\n",]
        self.incorrect = 0
    
    def get_art(self):
        if self.incorrect != 4:
            return"\n".join(self.art[self.incorrect:])
        return "   X\n" + "\n".join(self.art[self.incorrect + 1:])
    
    def guessed_wrong(self):
        self.incorrect += 1
    
    def get_incorrect(self):
        return self.incorrect