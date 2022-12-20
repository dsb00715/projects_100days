""" 3 kinds of coffee flavours:
Espresso(50ml Water, 18g Coffee)
Latte(200ml Water, 24g Coffee, 150ml Milk)
Cappuccino(250ml Water, 24g Coffee, 100ml Milk)

Storage Resources: 300ml Water, 200ml Milk, 100g Coffee

Coin Operated: Penny(1 cent)= $0.01, Nickel(5 Cents)= $0.05, Dime(10 cents)= $0.10, Quarter(25 cents)= $0.25

Program Requirements:
1. Print Report.
2. Check resources sufficient?
3. Process coins & calculate change.
4. Check transaction successful? - refund
5. Make Coffee. """

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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
