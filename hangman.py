"""
Todo
1. How to display the blanks and letters together? 
2. Along with missed letters.

Observation: The below code works in giving the output of letters guessed and the previously missed and guessed lettters.
But i am facing problems to extend it to add the below scenarios
1. I am not able to display the empty board with the number of 
2. Its different to find the alreadyguessed number from previously_guessed_blanks and missed_letters because they have '_'
in the list too..
    -Found a way to find it now
3. I am wondering how to not keep asking if i want to continue and ask it only when the game is over or options are over.
    -Added logic for checking if all the letters are correctly guessed or if maximum attempts are over. If any of this condition
    then game is over.
4. The board is not displayed before the message "you are out of attempts". I should be able to do that.
    - I should call th display board after all the attempts or when the user has won.
5. if i want to start the game over, then all the variables should be reset.
    - I can reassign all the variables as it is in the beginning
6. The hangman should be displayed in the board
    - I have made that happen
7. The secret word should be displayed after the game is over.
    - The secret word is displayed.
8. Dont allow anythin other than alphabets.
    - Added that condition to check if its part of string.ascii_letters.
9. Repetition of code for displaying the board.
    - created a new function to display the board.
10. Use strings instead of list for print the values.
    - 
"""
import random
from string import ascii_letters
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def get_random(words):
    wordindex = random.randint(0,len(words) - 1)
    return words[wordindex]

secret_word = get_random(words)
#secret_word = 'python'

def letters_with_blanks(blanks, secret, letter):
    indexes_to_replace = [ x for x,y in enumerate(secret) if secret[x] == letter]
    for i in indexes_to_replace:
        blanks[i] = letter
    return blanks

def guess_letter(already_guessed):
    while True:
        letter = input("Guess the letter: ")
        print()
        if letter in already_guessed:
            print("The letter is already provided, please enter another letter.")
        elif letter not in ascii_letters:
            print("Please enter an alphabet")
        else:
            return letter

def display_board(previous_value_blanks):
    print(HANGMAN_PICS[hangman_display])
    print("Word to be guessed:")
    print(previous_value_blanks)
    print("Missed Letters:")
    print(missed_letters)

previous_value_blanks = ["_" for i in range(len(secret_word))] 
correct_letters = []   
missed_letters = []
letter = ''
guessed_all = False
max_attempts = False
hangman_display = 0
play = 'yes'
while play:
    display_board(previous_value_blanks)
    letter = guess_letter(correct_letters + missed_letters)
    if letter in secret_word:
        previous_value_blanks = letters_with_blanks(previous_value_blanks, secret_word, letter)
        correct_letters.append(letter)
        if "_" not in previous_value_blanks:
            guessed_all = True
            print("You have guessed the correct word")
    else:
        missed_letters.append(letter)
        hangman_display += 1
        if len(missed_letters) >= len(HANGMAN_PICS) - 1:
            max_attempts = True
            print("You are out of attempts.")
    if guessed_all or max_attempts:
        display_board(previous_value_blanks)
        print("The secred word is: ", secret_word)
        play = input("Would you like to continue?")
        if play.lower() == 'no':
            break
        elif play.lower() == 'yes':
            previous_value_blanks = ["_" for i in range(len(secret_word))] 
            correct_letters = []   
            missed_letters = []
            letter = ''
            guessed_all = False
            max_attempts = False
            hangman_display = 0
    
        
