logo = """ ________                             ___________.__              _______               ___.                  
 /  _____/ __ __  ______ ____   ____   \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________  
/   \  ___|  |  \/  ___// __ \_/ __ \    |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \ 
\    \_\  \  |  /\___ \\  ___/\  ___/    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ 
 \______  /____//____  >\___  >\___  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|    
        \/           \/     \/     \/                  \/     \/          \/            \/    \/     \/    """

from random import randint

EASY_LEVEL_TURNS  =10
HARD_LEVEL_TURNS = 5
turns = 0
def check_answer(guess,answer,turns):
    if guess > answer:
        print("Too high")
       
        return turns-1
    elif guess < answer:
        print("Too Low")
        return turns -1
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS    


def game():
    print(logo)        
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. ")
    answer = randint(1,100)
    
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("make a guess: "))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You run out of guess. You lose.")
            return
        elif guess!= answer:
            print("Guess again!")    

game()