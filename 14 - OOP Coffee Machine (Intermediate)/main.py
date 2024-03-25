from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()  # Convert input to lowercase for case-insensitivity
    if choice == "off":
        is_on = False
    elif choice == "report":
        # Display reports for both coffee maker and money machine
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)

        if drink is None:
            print("Invalid choice. Please select a valid drink from the menu.")
        elif coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # Make the chosen drink if resources are sufficient and payment is successful
            coffee_maker.make_coffee(drink)
