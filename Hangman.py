# display a menu with at least 3 difficulty choices and ask the user
# to select the desired level
difficulty = "1" # sample data, normally the user should choose the difficulty



# STEP 2
# based on the chosen difficulty level, set the values 
# for the player's lives
word_to_guess = "Cairo" # sample data, normally the word should be chosen from the countries-and-capitals.txt
lives = 5 # sample data, normally the lives should be chosen based on the difficulty


# STEP 3
# display the chosen word to guess with all letters replaced by "_"
# for example instead of "Cairo" display "_ _ _ _ _"


# STEP 4
# ask the user to type a letter
# here you should validate if the typed letter is the word 
# "quit", "Quit", "QUit", "QUIt", "QUIT", "QuIT"... you get the idea :)
# HINT: use the upper() or lower() built-in Python functions


# STEP 5
# validate if the typed letter is already in the tried letters
# HINT: search on the internet: `python if letter in list`
# If it is not, than append to the tried letters
# If it has already been typed, return to STEP 5. HINT: use a while loop here
already_tried_letters = [] # this list will contain all the tried letters


# STEP 6
# if the letter is present in the word iterate through all the letters in the variable
# word_to_guess. If that letter is present in the already_tried_letters then display it,
# otherwise display "_".


# if the letter is not present in the word decrease the value in the lives variable
# and display a hangman ASCII art. You can search the Internet for "hangman ASCII art",
# or draw a new beautiful one on your own.



# STEP 7
# check if the variable already_tried_letters already contains all the letters necessary
# to build the value in the variable word_to_guess. If so display a winning message and exit
# the app.
# If you still have letters that are not guessed check if you have a non negative amount of lives
# left. If not print a loosing message and exit the app.
# If neither of the 2 conditions mentioned above go back to STEP 4


import random
def graf(lives):
    gallows_graf = [
    """
    -------
    |     |
    |     O
    |    /|\\
    |    / \\
    |
    -------
    """,
     """
    -------
    |
    |     O
    |    /|\\
    |    / \\
    |
    -------
    """,
     """
    -------
    |
    |
    |    /|\\
    |    / \\
    |
    -------
    """
    ,
     """
    -------
    |     |
    |
    |
    |
    |
    -------
    """
    ]
    return gallows_graf[lives]
def game(words: list, lives: int):
    word_to_guess = random.choice(words).upper()
    display_word = "_ " * len(word_to_guess)
    good_guesses = set()
    while lives > 0 and "_" in display_word:
        print(f"Try guessing: {display_word}")
        print(graf(lives))
        letter = input("Try to guess a letter: ").upper()
        if letter in word_to_guess:
            good_guesses.add(letter)
            display_word = ""
            for ch in word_to_guess:
                if ch in good_guesses:
                    display_word += ch
                else:
                    display_word += "_"
                display_word += " "
        else:
            lives -= 1
            if lives > 0:
                print(f"Wrong guess!!! You have still {lives} tries")
            else:
                print("You don't have any tries left...")
    
        if lives > 0:
            print("You won!!!")
        else:
            print("You lost the game!!!")


def main():
    capitals = [
        "Paris", "Berlin", "Rome", "Madrid", "London", "Athens",
        "Vienna", "Budapest", "Warsaw", "Lisbon", "Prague", "Stockholm",
        "Oslo", "Dublin", "Copenhagen",
    ]
    lives = 3
    answer = input("Do you want to start a new game? Y/N ")
    while answer.lower() == "y":
        game(capitals, lives)
        answer = input("Do you want to start a new game? Y/N ")
main()