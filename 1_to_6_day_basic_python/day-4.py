import random
"""

import my_module
random_integer = random.randint(1,10)
print(random_integer)
print(my_module.pi)

random_float = random.random()*5
print(random_float)
"""


"""
test_seed =  int(input("Create a seed number: "))
random.seed(test_seed)


random_side = random.randint(0,1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")    
"""

"""
test_seed =  int(input("Create a seed number: "))
random.seed(test_seed)

nameAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = nameAsCSV.split(", ")
x = len(names)
p = random.randint(0,x-1)
#p = random.choice(names)
print(names[p] + " is going to buy the meal.")
"""
"""
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
"""


import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0: 
    print("You typed an invalid number, you lose!") 
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")
