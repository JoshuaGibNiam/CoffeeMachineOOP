from Menu import Menu
from MoneyProcessor import MoneyMachine
from CoffeeMakerClass import CoffeeMaker

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

    if user_action == "off":
        break

    elif user_action == "report":
        coffeemachine.report()
        moneymachine.report()

    elif user_action == "admin":
        if adminaccess():
            admin_order = input("What would you like to do?: ")
            if admin_order == "add":
                menu.add_item()
            elif admin_order == "remove":
               menu.remove_item()
            else:
              continue
    else:
        order = menu.find_drink(user_action)
        if not order:
            print("Sorry, order does not exist.")
        else:
            if coffeemachine.resource_sufficient(order):
                if moneymachine.make_payment(order):
                    coffeemachine.make_coffee(order)
                else:
                    print("Payment unsuccessful. Skedaddle!")
            else:
                print("We're terribly sorry, our resource has been depleted.")

    print("\n\n")
