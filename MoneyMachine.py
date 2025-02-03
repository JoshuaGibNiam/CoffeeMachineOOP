class CoffeeMaker:
    """prints the resources in the coffee machine"""

    def __init__(self):
        self.resources = {'water': 1500, 'milk': 700, 'coffee': 200}

    def report(self):
        for k, i in self.resources.items():
            print(f"{k}: {i}ml" if k != 'coffee' else f"{k}: {i}g")

    def resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient"""
        for items in drink.ingredient:
            if drink.ingredient[items] > self.resources[items]:
                return False
        return True

    def make_coffee(self, drink):
        """Makes coffee and gives it to user"""
        for items in drink.ingredient:
            self.resources[items] -= drink.ingredient[items]
        print(f"Here's your {drink.name}. Enjoy!")
