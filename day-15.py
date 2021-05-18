MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0

def check_resources(drink):
    p  = MENU[drink]["ingredients"]

    for i in p:
        if p[i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return  True 

def deduct(drink):  
    p  = MENU[drink]["ingredients"]     
    for i in p:
        resources[i] -= p[i]          

def insertcoin():
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return 0.25*quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
           

run = True
while run:
    choice  = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'report':
        for i in resources:
            print(f'{i} : {resources[i]}')
        print(f"Money: ${money}")    
    elif choice == 'off':
        run = False        
    else:
        available =check_resources(choice)
        if available == True:
            print("Please insert coins.")
            total = insertcoin()
            if total < MENU[choice]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                deduct(choice)
                amount = abs(total - MENU[choice]["cost"])
                money += MENU[choice]["cost"]
                print(f"Here is ${amount} in change.")
                print(f"Here is your {choice} ☕️. Enjoy!")       
