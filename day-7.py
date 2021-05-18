import random
import hangman_words

from hangman_art import stages,logo

print(logo)
word_list = hangman_words.word_list

chosen_word = random.choice(word_list) 

end_of_game = False
lives = 6

display = ["_"]*len(chosen_word)
while not end_of_game: 
    guess = input("Guess a letter: ").lower()


    if guess in display:
        print(f"You have already guessed {guess}")    
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            
    if guess not  in chosen_word:
        print(f"You guessed {guess}, thats not in the word. You losse life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You Loose.')




            
      


    print(f"{''.join(display)}") 

    if "_" not in display:
        end_of_game = True 
        print("You Win.")  
    print(stages[lives])   