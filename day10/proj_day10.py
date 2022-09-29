# Commandline Calculator
from art import logo


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {"+": add, "-": sub, "*": mul, "/": div}  # to select function dynamically


def calculator():
    print(logo)  # Calculation Ascii art
    num1 = float(input("What's the first number?: "))
    for op in operations:
        print(op)  # This will print all 4 allowed operations
    cont = True

    while cont:  # Will run until user want's to exit and says 'n'
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        # Combination of two lines calculation_function = operations[operation_symbol] and second: result = calculation_function(num1,num2)
        result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        status = input(
            f"Type 'y' to continue Calculating with {result}, or type 'n' to start a new calculation or type 'e' to exit: "
        )
        if status == "y":
            num1 = result
        elif status == "n":
            cont = False  # Exit from the while loop
            calculator()  # Recursive function
        elif status == "e":
            break  # exit from recursive function


calculator()
