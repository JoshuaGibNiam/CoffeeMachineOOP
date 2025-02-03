# Coffee Machine Project - Object-Oriented Programming

---

## Description
This is a program simulating an automatic coffee machine. It is easy to use, and has basic features that all
coffee machine has (Maybe even better!).


## Features
1. **Order Coffee**: Allows user to order three types of coffee: espresso, latte, and cappuccino
2. **Make Payments**: Allows user to make payments using card or cash, keeps track of profits and prints receipts
3. **Report resources**: Allows user to check the resources in the coffee machine. (water, milk, and coffee)
4. **Turn off machine (admin function)**: Allows admin to turn off the machine.
5. **Add items to menu (admin function)**: Allows admin to add items to the menu.
6. **Remove items from menu (admin function)**: Allows admin to remove items from the menu.
7. **Add resources (admin function)**: Allows admin to add resources to the coffee machine.

## Usage
1. When you run the program, it will first ask for your order. Enter your order based on the menu. If there is a typo, 
the machine will ask you to enter again. If you want to check the resources in the machine, enter "report".
2. Next, the machine will ask for you to make your payment, by card or cash. For card, enter a 16 digit card number;
for cash, it will ask you for coins: Androllars (A$1), Andruaters (A$0.25), Andrickles (A$0.05), Andrennies (A$0.01).
It will handle changes if needed. Then, it will print your receipt.
3. To access admin features, enter "admin" at the start then enter "111222" as the password. Your admin functions
include:
 - "add": allows you to add an item to the menu. (You will need to enter its name and the resource needed to make it, and its cost.)
 - "remove": allows you to remove an item from the menu. (Enter its name)
 - "add resources": allows you to add resources to the coffee machine.
 - "off": allows you to turn off the machine completely.

---
Run the program at main.py 