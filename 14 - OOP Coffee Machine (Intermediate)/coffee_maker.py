class CoffeeMaker:
    def __init__(self):
        # Initialize resources for the coffee maker
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        # Print a report of available resources
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        # Check if there are enough resources to make a specific drink
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_coffee(self, order):
        # Make a coffee by deducting the required ingredients from resources
        if self.is_resource_sufficient(order):
            for item in order.ingredients:
                self.resources[item] -= order.ingredients[item]
            print(f"Here is your {order.name} ☕️. Enjoy!")
            return True
        else:
            print("Cannot make the coffee. Resources insufficient.")
            return False
