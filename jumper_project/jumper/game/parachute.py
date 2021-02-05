class Parachute:
    """A code template for a parachute that slowly dies. It's responsibility
    is to keep track of when it dies, and to look pretty
    
    Stereotype:
        Information Holder

    Attributes:
        art (list): the list of ascii art to display to the user.
        incorrect (number): The number of parachute parts that have been destroyed
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Parachute): An instance of Parachute.
        """
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
        """Gets the graphical display of remaining parachute parts.

        Args:
            self (Parachute): An instance of Parachute.
        
        Returns:
            string: ascii art of the remaining parachute.
        """
        if self.incorrect != 4:
            return"\n".join(self.art[self.incorrect:])
        return "   X\n" + "\n".join(self.art[self.incorrect + 1:])
    
    def guessed_wrong(self):
        """Increments the amount of damage the parachute has taken.

        Args:
            self (Parachute): An instance of Parachute.
        """
        self.incorrect += 1
    
    def is_dead(self):
        """States whether the parachute has been destroyed.

        Args:
            self (Parachute): An instance of Parachute.
        
        Returns:
            boolean: whether the parachute has been destroyed.
        """
        return self.incorrect >= 4