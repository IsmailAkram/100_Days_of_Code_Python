from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

MACHINE_RUNNING = True

while MACHINE_RUNNING:
    # TODO: 1 Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

    coffee_prompt = str(input(f"What would you like? ({menu.get_items()}): ")).lower()

    # TODO: 2 Turn off the Coffee Machine by entering "off" to the prompt.
    if coffee_prompt == "off":
        print("Turning off coffee machine")
        MACHINE_RUNNING = False

    elif coffee_prompt == "report":
    # TODO: 3 Print report
        coffee_maker.report()
        money_machine.report()

    else:
    # TODO: 4 Check resources sufficient?
        drink = menu.find_drink(coffee_prompt)
        if coffee_maker.is_resource_sufficient(drink):
    # TODO: 5 Process coins.
            print(f"That will be ${drink.cost}")
            # TODO: 6 Check transaction successful?
            if money_machine.make_payment(drink.cost):
                # TODO: 7 Make Coffee.
                coffee_maker.make_coffee(drink)



