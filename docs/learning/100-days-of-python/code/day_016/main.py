from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# Initialise objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# Set loop for the machine to serve the next customer (until an employee switches it off)
machine_on = True

while machine_on:

    # Ask the user for input
    user_input = input(f"What would you like? {menu.get_items()}: ").lower()

    # Employee feature - ask for report (money and resources)
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()

    # Employee feature - switch the machine off if needed
    elif user_input == "off":
        machine_on = False

    # If a drink value (or neither report/off features) is given, proceed with the core logic
    else:

        # Obtain an object for the required drink
        drink = menu.find_drink(user_input)

        # Check if there is such a drink
        if drink:

            # Check if there are sufficient resources to make this drink
            if coffee_maker.is_resource_sufficient(drink):

                # Ask the customer to insert coin, process them and check if transaction for successful
                if money_machine.make_payment(drink.cost):

                    # Make coffee
                    coffee_maker.make_coffee(drink)
