# Coffee Machine Project - Object-Oriented Programming  

## Description  
This program simulates an automatic coffee machine. It is easy to use and includes basic features found in all coffee machines—perhaps even better ones!  

## Features  
1. **Order Coffee**: Allows users to order three types of coffee: espresso, latte, and cappuccino.  
2. **Make Payments**: Allows users to make payments using a card or cash, keeps track of profits, and prints receipts.  
3. **Check Resources**: Enables users to check the machine’s resources, including water, milk, and coffee.  
4. **Turn Off Machine (Admin Function)**: Allows an admin to turn off the machine.  
5. **Add Items to Menu (Admin Function)**: Allows an admin to add new items to the menu.  
6. **Remove Items from Menu (Admin Function)**: Allows an admin to remove items from the menu.  
7. **Add Resources (Admin Function)**: Allows an admin to replenish the coffee machine’s resources.  

## Usage  
1. When you run the program, it will first ask for your order. Enter your choice based on the menu. If there is a typo, the machine will prompt you to enter it again. To check the machine’s resources, enter **"report"**.  
2. Next, the machine will ask you to make a payment, either by card or cash.  
   - **Card**: Enter a 16-digit card number.  
   - **Cash**: Insert coins: Androllars (A$1), Andruaters (A$0.25), Andrickles (A$0.05), and Andrennies (A$0.01). The machine will handle change if needed.  
   - A receipt will be printed after payment.  
3. To access admin features, enter **"admin"** at the start and input the password **"111222"**. The admin functions include:  
   - **"add"**: Add an item to the menu. (Enter its name, required resources, and cost.)  
   - **"remove"**: Remove an item from the menu. (Enter its name.)  
   - **"add resources"**: Replenish the coffee machine’s resources.  
   - **"off"**: Turn off the machine completely.  

---  
Run the program at **`main.py`**.  
