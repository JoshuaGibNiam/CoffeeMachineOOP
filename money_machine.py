from datetime import datetime as dt


class MoneyMachine:
    CURRENCY = "A$"
    COIN_VALUES = {"Androllars": 1, "Andruaters": 0.25, "Andrickles": 0.05,
                   "Andrennies": 0.01}

    def __init__(self):
        self.profit = 0
        self.total_value = 0

    def report(self):
        """REports profit made."""
        print(f"Profit: A${self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        self.total_value = 0
        for x, y in MoneyMachine.COIN_VALUES.items():
            self.coinvalue = int(input(f"How many {x} have you got?: "))
            self.coinvalue *= y
            self.total_value += self.coinvalue
        return self.total_value

    def process_card(self):
        """Processes card payment"""
        self.cardnumber = input("PLease enter card number(16 digits):")
        if self.cardnumber.isdigit() and len(self.cardnumber) == 16:

            print("Card accepted")
            return True
        else:
            print("Card denied!")
            return False

    def make_payment(self, drink):
        """Check if balance is sufficient to buy drink"""
        self.card_or_cash = input("Would you like to pay with card or cash?: ").lower()
        while self.card_or_cash != "card" and self.card_or_cash != "cash":
            self.card_or_cash = input("Invalid input. PLease enter card or cash: ")
        if self.card_or_cash == "cash":
            self.process_coins()
            if self.total_value == drink.cost:
                self.profit += drink.cost
                self.print_receipt(drink)
                print("Payment successful.")
                return True
            elif self.total_value > drink.cost:
                self.print_receipt(drink)
                print("Payment successful.")
                print(f"Here is A${round(self.total_value - drink.cost, 2)} in change.")
                self.profit += drink.cost
                return True
            else:
                return False
        else:
            if self.process_card():
                self.print_receipt(drink, int(self.cardnumber))
                return True
            else:
                return False

    def print_receipt(self, order, cardnumber=0):
        print("Receipt:")
        print(f"\nOrder for {order.name} made at {dt.now()} \n"
              f"A${order.cost} paid fully.")
        if cardnumber != 0:
            print(f"Order made by card: **** **** **** {str(cardnumber)[-4:]}\n")
        else:
            print("Order made by cash.\n")
