
"""
height = int(input("Enter your height "))
weight = float(input("Enter your weight "))

bmi = weight / height **2
print(int(bmi))
"""

"""
age = input("What is your current age?\n")
age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining*365
weeks_remaining = years_remaining*52
months_remaining = years_remaining*12
message = f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months"
print(message)
"""


print("Welcome to tip calculator!!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, 15\n"))
people = int(input("How many people to split the bill?\n"))
bill_with_tip = tip/100 * bill + bill
bill_per_person = bill_with_tip/people
print(f"Each person should pay: ${round(bill_per_person,2)}")


