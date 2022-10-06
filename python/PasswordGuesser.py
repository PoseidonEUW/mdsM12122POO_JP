# Password Guesser class
from PersonalInfo import PersonalInfo
import random
import string

class PasswordGuesser:
    def __init__(self, password):
        self.password = password
        self.guesses = 0

    def guess(self):
        self.guesses += 1
        return ''.join(random.choice(string.ascii_letters) for _ in range(len(self.password)))

    def get_guesses(self):
        return self.guesses

    def get_password(self):
        return self.password

    def is_correct(self, guess):
        return guess == self.password
