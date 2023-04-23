#Step 3
import hangman
import random
from word_hang import word_list

from os import system, name
play_again = "Y"

while play_again == "Y":
    system ('cls')
    print (hangman.logo)
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    #Testing code
    #print(f'Pssst, the solution is {chosen_word}.')
    #Create blanks
    display = []
    store = []
    for _ in range(word_length):
        display += "_"

    #TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

    end_game = False
    life = 6



    while not end_game:
        guess = input("Guess a letter: ").lower()
        #Check guessed letter
        system ('cls')
        print (hangman.HANGMANPICS[life])
        if guess in store:
            print (f"You have already guessed {guess}.")
        else:
            store.append(guess)
            for position in range(word_length):
                letter = chosen_word[position]
                #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
                if letter == guess:
                    display[position] = letter
            if guess not in chosen_word:
                life -= 1
                print ("----you didnt guess correct word. You loose a life-----")
            print(' '.join(display))

            if list(chosen_word) == display:
                print ("!!!!You Won!!!!")
                end_game = True
            if life == 0:
                print ("You lost")
                end_game = True
                print (f"The word is {chosen_word}") 
    
    play_again = input("Do you want to play again? (Y/N)\n").upper()
    