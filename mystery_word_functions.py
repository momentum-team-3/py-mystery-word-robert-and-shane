"""functions to be imported and used in mystery_word.py"""
# imports
import random
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
    while True:
        level = int(input('Choose a Difficulty (1 = Easy, 2 = Normal, 3 = Hard): '))
        if level > 0 and level <= 3:
            return level
        else:
            raise ValueError("Input must be 1, 2, 3")


#function to grab a word, by random, depending on the level the user chose as well
def get_difficulty_level(level: int, wordlist: list) -> str: 
    if level == 1:
        easy_wordlist = [word for word in wordlist if 4 <= len(word) <= 6]
        mystery_word = random.choice(easy_wordlist)
        return mystery_word
    elif level == 2:
            normal_wordlist = [word for word in wordlist if 6 <= len(word) <= 8]
            mystery_word = random.choice(normal_wordlist)
            return mystery_word
    elif level == 3:
            hard_wordlist = [word for word in wordlist if 8 <= len(word)]
            mystery_word = random.choice(hard_wordlist)
            return mystery_word
    #print(f'The Mystery word is{len(mystery_word)} letters long.')


#function to place spaces where the letter should be
def show_blanks_or_letters(mystery_word: str) -> str:
    outputlist = []
    for letter in mystery_word:
        if letter in previousguesses:
            outputlist.append(letter)
        else:
            outputlist.append('_')
    display_string= "".join(outputlist)
    return display_string

"""#function to take in user input
def User_guess(guess):
    if guess in mystery_word
        pass
    elif letter not in mystery_word:
        print("That letter is not in the Mystery Word, Try Again!")
        guessesRemaining -= 1
        pass 
"""


#function to check if guess has been previous guessed
def check_previous_guesses(guess):
    if guess in previousguesses:
        raise ValueError("This letter has already been guessed")
    else:
        previousguesses.append(guess)
        return guess


def get_player_guess():
    guess = input('Guess one letter').lower()
    if guess not in ascii_lowercase:
        raise ValueError("Input must be a single alphabetic character")
    elif len(guess) != 1:
        raise ValueError("Input must be a single alphabetic character")
    else:
        check_previous_guesses(guess)
        if guess in mysteryword:
            return #idk yet