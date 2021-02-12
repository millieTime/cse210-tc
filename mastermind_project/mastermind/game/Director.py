


def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        for x in range(2):
            name = self.console.print(f"Enter a name for player {x + 1}: ")
            player = Player(name)
            self.roster.add_player(player)