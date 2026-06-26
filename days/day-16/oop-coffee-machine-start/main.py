from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_menu = Menu()
machine_coffee_maker = CoffeeMaker()
machine_money_machine = MoneyMachine()

while True:
    options = machine_menu.get_items()
    choice = input(f"What would you like ({options}):")

    if choice == "off":
        break
    elif choice == "report":
        machine_coffee_maker.report()
        machine_money_machine.report()
    else:
        drink = machine_menu.find_drink(choice)
        if not machine_coffee_maker.is_resource_sufficient(drink):
            continue
        

        if not machine_money_machine.make_payment(drink.cost): # type: ignore
            continue
        machine_coffee_maker.make_coffee(drink)