from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

def adminaccess():
    pwd = input("Enter admin password: ")
    if pwd == "111222":
        print("Access granted!")
        return True
    else:
        print("Access denied!")
        return False

menu = Menu()
coffeemachine = CoffeeMaker()
moneymachine = MoneyMachine()

while True:
    print(menu.get_items())
    user_action = input("What would you like to order?: ").lower()

    if user_action == "report":
        coffeemachine.report()
        moneymachine.report()

    elif user_action == "admin":
        if adminaccess():
            admin_order = input("What would you like to do?: ").lower()
            if admin_order == "add":
                menu.add_item()
            elif admin_order == "remove":
               menu.remove_item()
            elif admin_order == "add resources":
                coffeemachine.add_resource()
            elif admin_order == "off":
                break
            else:
              continue
    else:
        order = menu.find_drink(user_action)
        if order is None:
            print(f"Sorry, {user_action} does not exist.")
        else:
            if coffeemachine.resource_sufficient(order):
                if moneymachine.make_payment(order):
                    coffeemachine.make_coffee(order)
                else:
                    print("Payment unsuccessful. Skedaddle!")
            else:
                print("We're terribly sorry, our resource has been depleted.")

    print("\n\n")
