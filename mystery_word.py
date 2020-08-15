"""
TO DO: Read in the file
  Input: File
  Output: List of Strings

def get_word_list(file)
with open(file) as infile:
    wordfile = infile.read()
    lowerfile = wordfile.lower()
    wordlist = lowerfile.split()
    return wordlist
  
  - should make lowercase
  - use .splt() to make a list

TO DO: Take user input about difficultly level. Conditionally start game. 
  Input: string
  Output: validated string

def validate_level():
    level_input = input('Choose a Difficulty (1 = Easy, 2 = Normal, 3 = Hard): ')
    level = level_input.lower()
        if level == 1 or 2 or 3:
            return level
        else:
            raise ValueError("Input must be 1, 2, 3")


        - clean input by making lowercase
        - validate input


TO DO: Function functions to use conditionally after user input.
  Input: String (easy,normal,hard)
  Output:
def get_difficulty_level(level): 
    if level == 1 :
        for word in wordlist
        if 4 <= len(word) <= 6
        word = random.choice(wordlist)
    elif level == 2 :
        for word in wordlist
        if 6 <= len(word) <= 8
        word = random.choice(wordlist)
    elif level == 3 :
        for word in wordlist
        if 8 <= len(word)
        word = random.choice(wordlist)
        return get_difficulty_level()
        print(f'The Mystery word is{len(word)} letters long.')
    
        - Word will be chosen by random from within their parameters
        - if input is easy then function pulls word with 4-6 characters
        - if input is normal then function pulls word with 6-8 characters
        - if input is hard then function pulls word with 8+ characters
        - Inform user how many letters are in the mystery word

TO DO: Write function to take player guess
  Input: string
  Output: ??
  
  def get_player_guess():
      guess = input('Guess one letter').lower()
      if guess not in ascii_lowercase:
            raise ValueError("Input must be a single alphabetic character")
      elif len(guess) != 1:
            raise ValueError("Input must be a single alphabetic character")
      else:
            check_previous_guesses(guess)
            if guess in mysteryword:
                **To be continued**

        - should be validated
        - validation should check if it is a single lowercase alpha character
          error should be given if multiple letters are guessed at once.
          player should be reprompted to guess one letter. 
        - check if guess is in "previous guess list" 
            - conditionally respond
                - if it is then use below check user guess function
                - if not move forward by adding it to the "previous guess list"
                  and use function to check if it is in the mystery word. 

TO DO: Write function to update user guess count
  Input: string 
  Output: Returned update to screen?

        - display and is updated after each guess
        - show the number of guess left
        - maybe a fun visual to take the place of the traditional hangman.


TO DO: Write function to check user guess (User starts with 8 guesses)
  Input:
  Output:
  
        - if input is wrong, notify user and take a guess away
        - if input is correct, user continues to guess and doesn't lose a guess.
        - if input is in "previous guess list", user doesn't lose a guess.

TO DO: Write function to check if the user guess is in the mystery word
  Input:
  Output:
        - should be used in the conditional statement inside the function to take 
          the players guess. 
        - conditionally check if player guess is in mystery word
            - write conditional statements or use function to update the display. 

To Do: Write function to add/check validated user guess to "previous guess list"
  Input:
  Output:

def check_previous_guesses(guess):
    if guess in previousguesses:
        raise ValueError("This letter has already been guessed")
    else:
        previousguesses.append(guess)
        return guess

        - check_previous_guesses(guess) **use this as the function name**

TO DO: write function to create intital display
  Input:
  Output:
    Suggestions: These could all be functions??
        - Should display _ for every letter in the mystery word
        - Should display guess count number and/or 
          a fun graphical representation. 
        - Prompt player to input a guess
        - Maybe display the "previous guess list"

TO DO: Write function to upate display based on letter being guessed
  Input:
  Output:
        - If letter has not been guessed, display _
            - (probably not necessary, because this is currently displayed)
        - If a letter has been guessed, _ should be replaced with all instances
           of that letter in the mystery word
        - this funciton should take vaildated input that has been checked
          against our previously guessed list of letters.
        - guess count should be updated, if user guesses wrong
        
TO DO: Write function for when the game ends
  Input:
  Output:

  def play_again():
    if input('Dare to try again? (yay/nay): ') == 'yay':
      new_word = get_difficulty_level()
      run_mystery_word(new_word)
      return
      
        - If the user runs out of guesses, notify them and display Mystery Word.
        - If user finishes the Myster Word, congratulate them
        - Prompt the user if they would like to play again

TO DO: Figure out where (what state) the "previous guess list" should live
  Input:
  Output:
        - Should create empty list previous_guesses = []
        - Will discouraged 'global' variables, so we just need to make
          the scope big enough to store our data, without living outside 
          our while loops. 
 """


# Game Code
# Imports
Import random
from mystery_word_functions import get_word_list, validate_level

def run_mystery_word (file):
    previousguesses = []
    pass


if __name__ == "__main__":
    import sys

    file = sys.argv[1]
    status, output_string = run_mystery_word(file)
    print(output_string)
    exit(status)


