class MenuItem:
    """Models each Menu item"""

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredient = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }


class Menu:
    """Models the menu with the drinks"""

    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3)
        ]

    def get_items(self):
        """Returns all the names of the available menu items and its price"""
        options = ""
        for item in self.menu:
            options += f"{item.name} : A${item.cost} / "
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name, returns it if it exists otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        return None

    def add_item(self):
        self.addname = input("What would you like to name your coffee?: ")
        self.water = int(input("How much water does it need?(ml): "))
        self.milk = int(input("How much milk does it need?(ml): "))
        self.coffee = int(input("HOw much coffee does it need?(g): "))
        self.cost = float(input("HOw much (A$) does it cost?: "))
        self.menu.append(MenuItem(self.addname, self.water, self.milk, self.coffee, self.cost))
        print(f"{self.addname} added!")

    def remove_item(self):
        self.removed_item = input("What would you like to remove?: ")
        self.removed_item = self.find_drink(self.removed_item)
        if self.removed_item:
            self.menu.remove(self.removed_item)
            print(f"{self.removed_item.name} successfully removed!")
        else:
            print("Sorry, that item does not exist.")
