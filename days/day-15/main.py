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


# TODO 3. Print report.
def report(machine_resources):
    return f"Water: {machine_resources['water']}\nMilk: {machine_resources['milk']}\nCoffee: {machine_resources['coffee']}"


# TODO 4. Check resources sufficient?
def resource_sufficiency(required_drink):
    """Checks if we have enough resources to make the required drink"""

    drink_ingredients = required_drink["ingredients"]
    for ingredient in drink_ingredients:
        if ingredient not in resources:
            continue
        if drink_ingredients[ingredient] > resources[ingredient]:
            return False

    return True


# TODO 5. Process coins.
def process_coins():
    """Get coins from user, Adds the coins and returns the value"""
    print("Please insert coins.")
    quarters = int(input("How many quarters inserted: "))
    dimes = int(input("How many dimes inserted: "))
    nickels = int(input("How many nickles inserted: "))
    pennies = int(input("How many pennies inserted: "))

    total = 0
    total += (quarters * 0.25)
    total += (dimes * 0.15)
    total += (nickels * 0.05)
    total += (pennies * 0.01)

    return total


# TODO 7. Make Coffee.
def make_drink(drink_choice):
    """Uses the resources to make the drink"""

    required_drink = MENU[drink_choice]
    drink_ingredients = required_drink["ingredients"]
    for ingredient in drink_ingredients:
        if ingredient not in resources:
            continue
        resources[ingredient] -= drink_ingredients[ingredient]

    resources["Money"] = 0.0
    resources["Money"] += required_drink["cost"]
    print(f"Here is your {drink_choice}. Enjoy!")


def transaction_sufficient(amount_inserted, drink_choice):
    """Checks whether the user inserted enough money"""
    return amount_inserted > drink_choice["cost"]


def get_user_choice():
    """Forces the user to choose from the available options."""
    options = ["report", "espresso", "latte", "cappuccino", "off"]
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice in options:
            return choice
        print("Your choice is invalid. Please choose from the options listed!")


def main():
    machine_running = True
    while machine_running:
        user_choice = get_user_choice()

        if user_choice == 'report':
            print(report(resources))
            continue
        if user_choice == "off":
            break

        if not resource_sufficiency(MENU[user_choice]):
            print("Sorry there is not enough water")
            continue

        user_amount = process_coins()
        if not transaction_sufficient(user_amount, MENU[user_choice]):
            print("Sorry that's not enough money. Money refunded.")
            continue

        change = round(user_amount - MENU[user_choice]['cost'], 2)
        print(f"Here is ${change} in change")
        make_drink(user_choice)


main()
