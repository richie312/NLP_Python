# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string
import os

os.getcwd()
os.chdir(r"C:\Users\Richie\Desktop\Python_MIT\problem set and sol_recursive")

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

def partial_words(secret_word,guessed_letters):
    result = ''
    for letter in secret_word:
        if letter in guessed_letters:
            result = result + letter
        else:
            result = result + ' '
    return result


def hangman():
    #Runs the hangman game.
    
    print ('Welcome to the game, Hangman!')
    secret_word = choose_word(wordlist)
    print ('I am thinking of a word that is ' + str(len(secret_word)) + ' letters long.')
    num_guesses = 8
    word_guessed = False
    guessed_letters = ''
    available_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                         'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                         's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # Letter-guessing loop. Ask the user to guess a letter and respond to the
    # user based on whether the word has yet been correctly guessed.
    while num_guesses > 0 and not word_guessed:
        print ('-------------')
        print ('You have ' + str(num_guesses) + ' guesses left.')
        print ('Available letters: ' + ''.join(available_letters))
        guess = input('Please guess a letter:')
        if guess not in available_letters:
            print ('Oops! You\'ve already guessed that letter: ' + partial_words(secret_word, guessed_letters))
        elif guess not in secret_word:
            num_guesses -= 1
            available_letters.remove(guess)
            print ('Oops! That letter is not in my word: ' + partial_words(secret_word, guessed_letters))
        else:
            available_letters.remove(guess)
            guessed_letters += guess
            print (-'Good guess: ' + partial_words(secret_word, guessed_letters))
        if secret_word == partial_words(secret_word, guessed_letters):
            word_guessed = True
    if word_guessed:
        print ('Congratulations, you won!')
    else:
        print ('Game over.')

hangman()













