import re
import random


class WordHandler:

    def __init__(self):
        self.words = ['dictionary', 'basketball',
                      'robinhood', 'hippo', 'rhinoceros', 'friend', 'movie', 'genius', 'heartattack', 'mountain', 'doorknob']
        self.selectedWord = self.getWord()
        self.guessedLetters = ['']
        self.word = len(self.selectedWord)
        self.hidden = ["_"] * self.word

    def getWord(self):
        self.selectedWord = random.choice(self.words)
        return self.selectedWord

    def checkLetter(self, userInput):
        return userInput in self.selectedWord

    def canBeGuessed(self, userInput):
        if userInput not in self.guessedLetters:
            self.guessedLetters.append(userInput)
            return True
        else:
            return False

    def word_display(self):
        for spot in re.finditer(self.guessedLetters[-1], self.selectedWord):
            index = spot.start()
            self.hidden[index] = self.guessedLetters[-1]
        printed_word = " ".join(self.hidden)
        return printed_word

    def wordFound(self):
        if "_" in self.hidden:
            return False
        else:
            return True
