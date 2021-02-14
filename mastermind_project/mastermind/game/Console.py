class Console:
    """Interaction with the user, both reads user input and writes system responses.
    
    Stereotype:
        Interfacer
    """
     
    def read(self, prompt):
        """Gets text input from the user through the screen.

        Args: 
            self (Console): An instance of Console.
            prompt (string): The prompt to display to the user.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)
        
    def write(self, text):
        """Displays the given text on the screen. 

        Args: 
            self (Console): An instance of Console.
            text (string): The text to display.
        """
        print(text)