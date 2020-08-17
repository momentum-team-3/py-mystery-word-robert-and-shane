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
def validate_level() -> int:
    while True:
        try:
            level = int(input('Choose a Difficulty (1 = Easy, 2 = Normal, 3 = Hard): '))
            if level > 0 and level <= 3:
                return level
            else:
                print("Input must be 1, 2, 3")
        except ValueError:
                print("")


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


# helper function to produce the displayed mytstery word with _ if letter not guessed
def show_blanks_or_letters(mystery_word: str, previousguesses: list) -> str:
    outputlist = []
    for letter in mystery_word:
        if letter in previousguesses:
            outputlist.append(letter)
        else:
            outputlist.append('_')
    display_string = "".join(outputlist)
    return display_string



#function to take in user input
def guess_count(guess: str, mystery_word: list) -> int:
    guessesRemaining = 8
    if guess in mystery_word:
        return guessesRemaining
    elif guess not in mystery_word:
        print("That letter is not in the Mystery Word, Try Again!")
        guessesRemaining -= 1
        return guessesRemaining 
                


# helper function to check if guess has been previous guessed
def check_previous_guesses(guess: str, previousguesses: list) -> str:
    if guess in previousguesses:
        raise ValueError("This letter has already been guessed")
    else:
        previousguesses.append(guess)
        return guess

# helper function to get the players guess
def get_player_guess(mystery_word: str, previousguesses: list) -> str:
    guess = input('Guess one letter   ').lower()
    if guess not in ascii_lowercase:
        raise ValueError("Input must be a single alphabetic character")
    elif len(guess) != 1:
        raise ValueError("Input must be a single alphabetic character")
    else:
        check_previous_guesses(guess, previousguesses)
        if guess in mystery_word:
            return guess

# Looping to handle guessing
def gameplay_loop(mystery_word: str):
    previousguesses = []
    print(f"The mystery word is {len(mystery_word)} letters")
    gameplay = False
    while gameplay == False:
        guess = get_player_guess(mystery_word, previousguesses)
        count_display = guess_count(guess, mystery_word)
        word_display = show_blanks_or_letters(mystery_word, previousguesses)
        print(f"You have {count_display} guesses left!")
        print(f"{word_display}")
        if mystery_word == word_display:
            gameplay = True
            return "You Win!!!"
    