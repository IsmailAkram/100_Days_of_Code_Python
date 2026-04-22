from csv import excel

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
measurements = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
}
money = {
    "value": 0,
}

def report_resources():
    for key, value in resources.items():
        unit = measurements.get(key, "units") # Get the specific unit, default to "units" if key is not found
        print(f"{key}: {value}{unit}")

# TODO: 4. Check resources sufficient?
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

# TODO: 5 Process coins
def process_coins(quarter, dime, nickel, penny):
    """Returns the total cash calculated from coins inserted."""
    quarter *= 0.25
    dime *= 0.1
    nickel *= 0.05
    penny *= 0.01

    total_cash = quarter + dime + nickel + penny
    return total_cash

def make_coffee(order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

def coffee_machine():
    machine_running = True

    while machine_running:
            # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):"
            coffee_prompt = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()

            # TODO: 3. Print report of all coffee machine resources
            if coffee_prompt == "report":
                report_resources()
                print(f"Profit: ${money["value"]}")
            # TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt.
            elif coffee_prompt == "off":
                print("Shutting down coffee machine")
                machine_running = False
            elif coffee_prompt in MENU:
                cafe = MENU[coffee_prompt] # ingredients and cost

                try:
                    if check_resources(cafe["ingredients"]):
                        quarters = int(input("Please insert quarters: "))
                        dimes = int(input("Please input dimes: "))
                        nickles = int(input("Please input nickels: "))
                        pennies = int(input("Please input pennies: "))
                        cash = process_coins(quarters, dimes, nickles, pennies)

                        # TODO: 6. Check transaction successful?
                        # TODO: 7. Make coffee
                        if cash < cafe["cost"]:
                            print("Sorry that's not enough money. Money refunded.")
                        elif cash > cafe["cost"]:
                            change = cash - cafe["cost"]
                            money["value"] += cash - change
                            print(f"Here is ${round(change, 2)} dollars in change.")
                            print(f"Here is your {coffee_prompt} ☕ Enjoy!")
                            make_coffee(cafe["ingredients"])  # using ingredients from resources
                        else:
                            money["value"] += cash
                            print(f"Here is your {coffee_prompt} ☕ Enjoy!")
                            make_coffee(cafe["ingredients"]) # using ingredients from resources
                    else:
                        report_resources()
                        machine_running = False
                except ValueError as e:
                    print(f"Invalid input as: {e}")
            else:
                print("Invalid input. Try again.")



coffee_machine()