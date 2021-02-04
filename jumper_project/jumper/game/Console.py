class console:
    """
    responsibility of this class is to take user input and print the programs reactions.

    steriotype: interface
    attributes: prompt(information we display on each line)
    """

    def read(prompt):
        """
        args:
         self: instance of screen 
            prompt: the text to display to the user
        Returns:
            returns user input as string
        """
        resume = False
        while not resume:
            user_input = input(prompt)
            if user_input.isalpha() == True:
                return user_input.lower()

    def write(self,give):
        """
        args:
            self: screen instance
            give: desired print statement
        """
        print(give)
guess = console.read("guess a letter")
print(guess)