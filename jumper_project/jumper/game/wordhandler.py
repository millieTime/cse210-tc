import re
import random

class WordHandler:
    """A code template to choose a word from a list of words everything we need from the word
    ex) a character within a word, if that character has been guessed, if that character is right or wrong
    and if there are no more characters to be guessed, meaning the word is filled.

    Attributes:
        words (List): a list of random, hard-coded, words.
        selectedWord (String): the word for the user to guess.
        guessedLetters (List): a list of already guessed letters.
        hidden (List): a list of dashes to be replaced with correct letters.
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (WordHandler): an instance of WordHandler.
        """

        self.words = ['dictionary', 'basketball',
                      'robinhood', 'hippo', 'rhinoceros', 'friend', 'movie', 'genius', 'heartattack', 'mountain', 'doorknob']
        self.selectedWord = self.getWord()
        self.guessedLetters = ['_']
        self.hidden = ["_"] * len(self.selectedWord)

    def getWord(self):
        """Generates and picks a random word from the words list

        Args:
            self (WordHandler): an instance of WordHandler.
        """

        self.selectedWord = random.choice(self.words)
        return self.selectedWord

    def checkLetter(self, userInput):
        """Checks the letter guessed by the user to see if it's in the word.

        Args:
            self (WordHandler): an instance of WordHandler.
            userInput (String): the guessed letter.
        """

        return userInput in self.selectedWord

    def canBeGuessed(self, userInput):
        """Checks the letter and if it's already been guessed or not

        Args:
            self (WordHandler): an instance of WordHandler.
            userInput (String): the guessed letter.
        """

        if userInput not in self.guessedLetters:
            self.guessedLetters.append(userInput)
            return True
        else:
            return False

    def word_display(self):
        """Displays the word to the user. First off as a bunch of hidden letters and reveals the word as letters are guessed.

        Args:
            self (WordHandler): an instance of WordHandler.
        """
        for spot in re.finditer(self.guessedLetters[-1], self.selectedWord):
            index = spot.start()
            self.hidden[index] = self.guessedLetters[-1]
        printed_word = " ".join(self.hidden)
        return printed_word

    def wordFound(self):
        """Tells whether there are no more hidden letters, meaning that the word has been found!

        Args:
            self (WordHandler): an instance of WordHandler.
        """

        if "_" in self.hidden:
            return False
        else:
            return True
