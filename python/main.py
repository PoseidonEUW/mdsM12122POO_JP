# Main Python File

import sys
import os
import time
import random
import string
from PasswordGuesser import PasswordGuesser
from PersonalInfo import PersonalInfo

def main():
    # Get the password from the command line
    name = input("Enter your name")
    date = input("Enter your date of birth")
    user_password = input("Enter your password")
    person = PersonalInfo(name,date,user_password)
    # Create a PasswordGuesser object
    password = user_password
    guesser = PasswordGuesser(password)

    while True:
        guess = guesser.guess()
        if guesser.is_correct(guess):
            print("Password found: %s" % guess)
            print("Took %d guesses" % guesser.get_guesses())
            sys.exit(0)

        print("Tried: %s" % guess)

if __name__ == "__main__": main()
