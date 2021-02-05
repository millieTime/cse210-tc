class Console:
    """
    responsibility of this class is to take user input and print the programs reactions.

    steriotype: interface
    attributes: prompt(information we display on each line)
    """

    def read_input(self,prompt):
        """
        args:
         self: instance of screen 
            prompt: the text to display to the user
        Returns:
            returns user input as string
        """
        acceptable = False
        while not acceptable:
            user_input = input(prompt)
            if user_input.isalpha() and len(user_input) == 1:
                return user_input.lower()

    def write(self,give):
        """
        args:
            self: screen instance
            give: desired print statement
        """
        print(give)