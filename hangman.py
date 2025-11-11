import random
from hangman_art import logo, hangman_stages
from wordList import word_list

#import logo from hangman_art.py
print(logo)


guess_word = random.choice(word_list)

#Created placeholder
placeholder = ['_'] * len(guess_word)
placeholderdisplay = ''.join(placeholder)
print(placeholderdisplay+"\n")

already_guessed = []
count = 0
hangman_stage = 0
while count < len(guess_word):

    print(f"********************** {6-hangman_stage}/6 LIVES LEFT***********************************")
    letter = input("Guess a letter: ").lower()

    
    if letter not in already_guessed and letter in guess_word:
        already_guessed.append(letter)
        print(hangman_stages[hangman_stage])
    elif letter in already_guessed and letter in guess_word:
        print(f"You've already guessed {letter}")
        print(hangman_stages[hangman_stage])
    else:
        hangman_stage += 1
        print(f"You guessed {letter}, that's not in the word. You lose a life")
        print(hangman_stages[hangman_stage])
    
    
    for i in range(len(guess_word)):

        if guess_word[i] == letter:
            placeholder[i] = letter
        
        
        count = len(placeholder) - placeholder.count('_')
                                
    print(''.join(placeholder)+"\n")

    if hangman_stage == 6:
        print(f"*******************************************IT WAS {guess_word}, You Dead!!!**************************************")
        break
    if count == len(placeholder):
        print("*******************************************You Won!!!!**************************************")
        break

    


