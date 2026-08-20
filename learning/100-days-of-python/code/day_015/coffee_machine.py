from menu import MENU, resources


def format_data(resources):
    """Format resources data for printing the report."""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g"

def check_if_sufficient_resources(resources, menu, drink):
    """Check if we have enough resources to make customer a drink."""
    ingredients = menu[drink]["ingredients"]
    if drink != "espresso":
        if resources["milk"] < ingredients["milk"]:
            return "Sorry, there is not enough milk."
    
    if resources["water"] < ingredients["water"]:
        return "Sorry, there is not enough water."
    elif resources["coffee"] < ingredients["coffee"]:
        return "Sorry, there is not enough coffee."
    # return None if the coffee machine has enough resources
    return None

def ask_for_coins():
    print("Please insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    return quarters, dimes, nickles, pennies

def process_coins(quarters, dimes, nickles, pennies):
    quarters_total = quarters * 0.25
    dimes_total = dimes * 0.10
    nickles_total = nickles * 0.05
    pennies_total = pennies * 0.01
    money_total = float(quarters_total + dimes_total + nickles_total + pennies_total)
    return money_total

def check_if_sufficient_money(user_money, menu, drink):
    if user_money >= menu[drink]["cost"]:
        return True
    else:
        return False

def calculate_change(user_money, menu, drink):
    if user_money > menu[drink]["cost"]:
        change = float(user_money - menu[drink]["cost"])
        return change
    else:
        return None

def deduct_resources(resources, menu, drink):
    ingredients = menu[drink]["ingredients"]
    if drink != "espresso":
        resources["milk"] -= ingredients["milk"]
    resources["water"] -= ingredients["water"]
    resources["coffee"] -= ingredients["coffee"]
    return resources


# define starting loop and resources
is_on = True
money = 0

# keep asking until the customer exits
while is_on:

    # formatting resouces for the report
    formatted_resources = format_data(resources) + f"\nMoney: ${money}"

    # ask user what they want with "What would you like? (espresso/latte/cappuccino): "
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # turn off the coffee machine by entering “off” to the prompt
    if user_input == "off":
        is_on = False

    # print report
    elif user_input == "report":
        print(formatted_resources)

    # process espresso
    elif user_input in MENU:
        # check resources once; returns a message if short, else None
        insufficient_message = check_if_sufficient_resources(resources, MENU, user_input)
        if insufficient_message is not None:
            print(insufficient_message)
        else:
            # sk the customer to insert coins
            quarters, dimes, nickles, pennies = ask_for_coins()
            
            # calculate the total amount of customer's money
            user_money = process_coins(quarters, dimes, nickles, pennies)

            # check if the customer has enough money
            if not check_if_sufficient_money(user_money, MENU, user_input):
                print("Sorry that's not enough money. Money refunded.")
            
            # proceed to making the drink and adding the money to the machine + give change if any
            else:
                # add money to the coffe machine
                money += MENU[user_input]["cost"]
                
                # update coffee machine's resources
                resources = deduct_resources(resources, MENU, user_input)

                # if there is any change, give it back to the customer
                change = calculate_change(user_money, MENU, user_input)
                if change is not None:
                    print(f"Here is ${round(change, 2)} dollars in change.")
                
                print(f"Here is your {user_input}. Enjoy!")
                



