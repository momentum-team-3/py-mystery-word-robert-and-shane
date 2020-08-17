import random
import string

file = open("words.txt")
text = file.read().split()
file.close()

easy_level = [
    word.lower()
    for word in text
    if 4 <= len(word) <= 6
]

normal_level = [
    word.lower()
    for word in text
    if 6 <= len(word) <= 8
]

hard_level = [
    word.lower()
    for word in text 
    if 8 <= len(word)
]

guess_list = []

def get_level_difficulty():
    level = input('Please select a level (e - Easy, n - Normal, h - Hard): ')
    if level == 'e':
        word = random.choice(easy_level)
    elif level == 'n':
        word = random.choice(normal_level)
    elif level == 'h':
        word = random.choice(hard_level)
    else:
        return get_level_difficulty()
    print(f'The mystery word is {len(word)} characters long.')
    return word

    
def get_guess_list(guess_list):
    guess = input('Guess a letter: ').lower()
    if len(guess) != 1:
        print('Please guess a single letter.')
    else: 
        guess_list.append(guess)
    return guess_list

def display_word(word, guess_list):
    return (letter if letter in guess_list else '_' for letter in word)

def wrong_guesses(word, guess_list):
    return sorted(set(
        letter
        for letter in guess_list
        if not letter in word
    ))

def Game_Loop(word):
    guess_list = []
    while True:
        guesses_remaining = 8 - len(wrong_guesses(word, guess_list))
        print(f'WASTED LETTERS: {" ".join(wrong_guesses(word, guess_list))}.')
        print(f'Mystery Word: {" ".join(display_word(word, guess_list))}')
        print(f'You have {guesses_remaining} guesses remaining.')
        if '_' not in display_word(word, guess_list):
            print(f'CONGRATULATIONS, the Mystery Word was {word}')
            play_again()
            return
        if guesses_remaining == 0:
            print(f'YOU LOSE, the Mystery Word was {word}.')
            play_again()
            return
        guess_list = get_guess_list(guess_list)

def play_again():
    if input('CARE TO TRY AGAIN!? (y/n): ') == 'y':
        new_word = get_level_difficulty()
        Game_Loop(new_word)
    return

if __name__ == '__main__':
    word = (get_level_difficulty())
    Game_Loop(word)