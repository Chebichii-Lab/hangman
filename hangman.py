import random
from words import words

def get_valid_word(words):
    word = random.choice(words) # takes in a list and randomly chooses something from the list

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word
