class Console:
    """
    responsibility of this class is to take user input and print the program's reactions.

    stereotype: interface
    attributes: none
    """

    def read_letter(self,prompt):
        """Gets a single letter as input from the user

        args:
            self: instance of console
            prompt: the text to display to the user
        Returns:
            returns user input as string
        """
        acceptable = False
        while not acceptable:
            user_input = input(prompt)
            if user_input.isalpha() and len(user_input) == 1:
                return user_input.lower()
            print("Try entering a single letter. . .")

    def write(self,give):
        """Prints to the screen
        args:
            self: instance of Console
            give: desired print statement
        """
        print(give)
