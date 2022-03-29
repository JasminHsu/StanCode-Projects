"""
File: hangman.py
Name: Jasmin Hsu
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Repeatedly ask user to guess a character and compare
    the character with the random word till user figures
    out the whole word or runs out of the guess chances.
    During the guess process:
    If the character is in the word (match), shows the
    position of character. If not (not match), deduct a
    chance
    """
    word = random_word()
    look = str('-') * len(word)  # What the word looks like
    num_left = N_TURNS
    while True:
        print('The word looks like: '+str(look))
        print('You have '+str(num_left)+' guesses left.')
        guess = str(input('Your guess: ')).upper()  # Case-insensitive
        while True:  # To determine if the input format is correct (one character)
            if len(guess) != 1 or guess.isalpha() == False:
                print('illegal format.')
                guess = str(input('Your guess: ')).upper()
            else:
                break
        if word.find(guess) == -1 and num_left == 1:  # Not match and about to run out of chances
            print("There is no "+str(guess)+"'s in the word.")
            print('You are completely hung : (')
            print('The word was: '+str(word))
            break
        elif word.find(guess) == -1:  # Not match but still got chances
            print("There is no "+str(guess)+"'s in the word.")
            num_left -= 1
        elif word.find(guess) != -1:  # Match
            print('You are correct!')
            for i in range(len(word)):  # Show the position of matched character
                ch = word[i]
                if guess == ch:
                    look = look[:i] + guess + look[i+1:]
            if word == look:  # The whole word is figured out
                print('You win!!')
                print('The word was: ' + str(word))
                break


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
