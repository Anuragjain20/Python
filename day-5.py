
""""
student_heights = input("Input a list of student heights ").split()
for n in range(len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights) 

total_height = 0
number_of_students = len(student_heights)
for height in student_heights:
    total_height+=height
#print(total_height)    
average_height = round(total_height/number_of_students,2)
print(average_height)
"""

"""
for  number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')    
    
    elif number % 3 == 0:
        print('Fizz')

    elif number % 5 == 0:
        print('Buzz')

    else:
        print(number)    


"""
import random
import string
letters = list(string.ascii_letters) 
numbers = [str(i) for i in range(10)]
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input('How many symbols would you like?\n'))
nr_numbers = int(input('How many numbers would you like?\n'))


#Eazy_level
"""
password = ""

for char in range(1,nr_letters+1):
    random_char = random.choice(letters)
    password += random_char

for char in range(1,nr_symbols+1):
    password += random.choice(symbols)

for char in range(1,nr_numbers+1):
    password += random.choice(numbers)


print(password)
"""
#Hard_level

password = []
for char in range(1,nr_letters+1):
    random_char = random.choice(letters)
    password.append(random_char)

for char in range(1,nr_symbols+1):
    password.append(random.choice(symbols))

for char in range(1,nr_numbers+1):
    password.append(random.choice(numbers))

random.shuffle(password)

passw = ''.join(password) 
print("Your password is : "+passw)





