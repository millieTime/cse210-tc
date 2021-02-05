import random


class WordHandler:

    def __init__(self):
        self.words = ['dictionary', 'basketball',
                      'robinhood', 'hippo', 'rhinoceros', 'friend', 'movie', 'genius', 'heartattack', 'mountain', 'doorknob']
        self.selectedWord = self.getWord()
        self.guessedLetters = []

    def getWord(self):
        self.selectedWord = random.choice(self.words)
        return self.selectedWord

    def checkLetter(self, userInput):
        return userInput in self.selectedWord

    def hasBeenGuessed(self, userInput):
        if userInput not in self.guessedLetters:
            self.guessedLetters.append(userInput)
            return True
        else:
            return False
