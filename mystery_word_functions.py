"""functions to be imported and used in mystery_word.py"""
# imports

from string import ascii_lowercase

#function to read file and return list of words
def get_word_list(file: str) -> list:
    with open(file) as infile:
        wordfile = infile.read()
        lowerfile = wordfile.lower()
        wordlist = lowerfile.split()
        return wordlist


#function to validate player input about level and return level or error
def validate_level():
    level = input('Choose a Difficulty (1 = Easy, 2 = Normal, 3 = Hard): ')
        if level > 0 or level <= 3:
            return level
        else:
            raise ValueError("Input must be 1, 2, 3")


#function to check if guess has been previous guessed
def check_previous_guesses(guess):
    if guess in previousguesses:
        raise ValueError("This letter has already been guessed")
    else:
        previousguesses.append(guess)
        return guess