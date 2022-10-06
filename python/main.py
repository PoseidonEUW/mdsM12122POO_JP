# Main Python File

import sys
import os
import time
import random
import string

from PasswordGuesser import PasswordGuesser

def main():
    # Get the password from the command line
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <password>")
        sys.exit(1)
    password = sys.argv[1]
    guesser = PasswordGuesser(password)

    while True:
        guess = guesser.guess()
        if guesser.is_correct(guess):
            print("Password found: %s" % guess)
            print("Took %d guesses" % guesser.get_guesses())
            sys.exit(0)

        print("Tried: %s" % guess)

if __name__ == "__main__": main()
