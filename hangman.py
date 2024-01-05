import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # takes in a list and randomly chooses something from the list

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase) #alphabet
    used_letters = set() #what the user has guessed
