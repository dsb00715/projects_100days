# NOTE: Program Requirements:
# [x]TODO-1: Prompt user by asking “​What would you like? (espresso/latte/cappuccino):​
# [x]TODO-2: Turn off the Coffee Machine by entering "Off" to the prompt
# [x]TODO-3: Print Report
# [x]TODO-4: Check if Resources are sufficient?
# [x]TODO-5: Process Coins
# [x]TODO-6: Check if transaction if successful?
# [x]TODO-7: Make Coffee
# [x]TODO-8: Make Sure all requirements are met & Code is working as per requirement

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo


def main():
    print(logo)
    is_machine_on = True
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    while is_machine_on:

        user_ip = input(f"What would you like?({menu.get_items()}): ").lower()
        if user_ip == "off":
            is_machine_on = False
        elif user_ip == "report":
            coffee_maker.report()
            money_machine.report()
        elif user_ip == "espresso" or user_ip == "latte" or user_ip == "cappuccino":
            order_item = menu.find_drink(user_ip)
            if coffee_maker.is_resource_sufficient(order_item):
                if money_machine.make_payment(order_item.cost):
                    coffee_maker.make_coffee(order_item)


if __name__ == "__main__":
    main()
