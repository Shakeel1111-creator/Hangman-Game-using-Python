#Hangman Game

#Hangman Game

import random
words=['python','java','ruby','javascript','kotlin']
choosen=random.choice(words)
word_display=['-' for i in choosen]
attempts=9
print("Welcome to Hangman")

while attempts>0 and '-' in word_display:
    print('\n' +' '.join(word_display))
    guess=input("Guess a letter:").lower()
    if guess in choosen:
        for index,letter in enumerate(choosen):
            if letter==guess:
                word_display[index]=guess
    else:
        print("That letter doesn't appear in the word")
        attempts-=1


if '-' not in word_display:
    print("Your guessed the word!")
    print(' '.join(word_display))
    print("You survived")
else:
    print("You lost")
