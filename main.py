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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def is_resource_sufficient(order_ingredients):
    """Return true when order can be made, false if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def is_transaction_successfull(money_receive, drink_cost):
    """Return true if payment is accepted, and false if payment is not suffient to make the drink """
    if money_receive >= drink_cost:
        change = round(money_receive - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money.Money refunded")


def process_coins():
    '''It will return the total calculations from coins inserted'''
    print("Please insert coins")
    total = int(input("how many quarters?: "))*0.25
    total += int(input("how many dimes?: "))*0.1
    total += int(input("how many nickels?: "))*0.05
    total += int(input("how many pennies?: "))*0.01
    return  total

def make_coffe(drink_name, order_ingredient):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink_name}☕")


is_on = True

while is_on:
    choice = input("What would you like?(espresso, latte, capuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successfull(payment, drink['cost']):
                make_coffe(choice, drink["ingredients"])
