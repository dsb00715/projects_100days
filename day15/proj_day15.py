"""Coin Operated: Penny(1 cent)= $0.01, Nickel(5 Cents)= $0.05, Dime(10 cents)= $0.10, Quarter(25 cents)= $0.25"""
# NOTE: Program Requirements:
# [x]TODO-1: Prompt user by asking “​What would you like? (espresso/latte/cappuccino):​
# [x]TODO-2: Turn off the Coffee Machine by entering "Off" to the prompt
# [x]TODO-3: Print Report
# [x]TODO-4: Check if Resources are sufficient?
# [x]TODO-5: Process Coins
# [x]TODO-6: Check if transaction if successful?
# [x]TODO-7: Make Coffee
# [x]TODO-8: Make Sure all requirements are met & Code is working as per requirement

from coffee_menu import MENU


def show_report(resources, money):
    """Prints the report of resources!"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def process_coins():
    """Processes coins & returns total"""
    coins_d = {"quarters": 0, "dimes": 0, "nickles": 0, "pennies": 0}
    for key in coins_d:
        coins_d[key] = int(input(f"how many {key}?"))
    total = (
        (coins_d["quarters"] * 0.25)
        + (coins_d["dimes"] * 0.10)
        + (coins_d["nickles"] * 0.05)
        + (coins_d["pennies"] * 0.01)
    )
    return total


def make_coffee(resources, coffee_type, money_earned):
    """This function generates coffee if resources are available & enough price is paid!"""
    required_resources = MENU[coffee_type]["ingredients"]
    required_money = MENU[coffee_type]["cost"]
    for key in required_resources:
        if resources[key] < required_resources[key]:
            print(f"Sorry there is not enough {key}")
            return money_earned
    total_value = process_coins()
    if total_value < required_money:
        print("Sorry that's not enough money. Money refunded.")
        return money_earned
    else:
        money_earned += required_money
        refund_amount = round(total_value - required_money, 2)
        if refund_amount > 0:
            print(f"Here is ${refund_amount} in change.")
        for key in required_resources:
            resources[key] = resources[key] - required_resources[key]
        print(f"Here is your {coffee_type} ☕. Enjoy!")
        return money_earned


def main():
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    money_earned = 0
    available = True
    while available:
        user_ip = input("What would you like?(espresso/latte/cappuccino): ").lower()
        if user_ip == "off":
            available = False
        elif user_ip == "report":
            show_report(resources=resources, money=money_earned)
        elif user_ip == "espresso" or user_ip == "latte" or user_ip == "cappuccino":
            # money_earned, resources = make_coffee(
            #     resources=resources, coffee_type=user_ip, money_earned=money_earned
            # )
            money_earned = make_coffee(
                resources=resources, coffee_type=user_ip, money_earned=money_earned
            )


if __name__ == "__main__":
    main()
