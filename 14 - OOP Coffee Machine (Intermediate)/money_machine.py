class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        # Initialize the money machine with profit and money received
        self.profit = 0
        self.money_received = 0

    def report(self):
        # Print the current profit
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        # Process coins inserted by the user and return the total calculated
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        # Make a payment; return True if payment is accepted, False if insufficient
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is your {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            self.money_received = 0
            return False
