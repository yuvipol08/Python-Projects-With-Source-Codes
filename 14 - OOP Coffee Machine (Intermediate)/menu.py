class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        # Initialize a menu item with its name, ingredients, and cost
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    def __init__(self):
        # Initialize the menu with predefined drinks
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        # Return the names of all available menu items as a formatted string
        options = [item.name for item in self.menu]
        return "/".join(options)

    def find_drink(self, order_name):
        # Search for a drink by name in the menu; return None if not found
        for item in self.menu:
            if item.name.lower() == order_name.lower():  # Make the search case-insensitive
                return item
        print("Sorry, that item is not available.")
        return None  # Return None for invalid choices
