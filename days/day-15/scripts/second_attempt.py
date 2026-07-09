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
profit = 0.0
options = {
    "report": "Shows Current Machine Resources", 
    "espresso": "Request for espresso", 
    "latte": "Request for latte", 
    "cappuccino": "Request for cappuccino", 
    "off": "Turn the machine off", 
    "options": "Show all available options"
}


def show_report():
    print("\n=================================  Here are the Resources  ====================================\n\n")
    
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")

    print("\n")


def get_user_choice():
    """Gets choice from user and returns it."""
    while True:
        user_choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice in options.keys():
            return user_choice
        print("Your choice is invalid. Please choose from the options listed!")


def transaction_success(amount, drink_choice):
    """Return True if user inserted enough money, otherwise False"""

    drink_cost = drink_choice["cost"]
    if amount >= drink_cost:
        change = round(amount - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True

    return False


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def resource_sufficiency(chosen_drink):
    """Checks if we have enough resources to make the required drink"""

    drink_ingredients = chosen_drink["ingredients"]
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def make_coffee(drink_ingredients: dict, user_choice):
    """Deduct the required ingredients from the resources."""
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {user_choice} ☕️. Enjoy!")


def show_options():
    """This prints all the available options for the coffee machine"""
    print("\n=================================  Here are the Available Options  ====================================\n\n")
    for option in options.keys():
        print(f"{option.capitalize()}   ->   {options[option]}", end="\n")
    print("\n")

while True:

    choice = get_user_choice()

    if choice == "report":
        show_report()
        continue
    elif choice == "options":
        show_options()
        continue
    elif choice == "off":
        break
    else:
        drink = MENU[choice]
        if not resource_sufficiency(drink):
            continue

        amount_inserted = process_coins()
        if not transaction_success(amount_inserted, drink):
            continue
    make_coffee(drink["ingredients"], choice)
