""" 
# 1.

def greet(name):
    print(f"Hello {name}")
    print("what's up?")
    print("How's life?")


greet("Deep") """

# ***************************************************************************

""" # 2.
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"oh you're from {location}. What a lovely country!")


greet_with("Deep", "Germany")
greet_with(location="Germany", name="Shraddha") """

# ***************************************************************************

""" # 3.
# Write your code below this line 👇
from math import ceil


def paint_calc(height, width, cover):
    cans = ceil((height * width) / cover)
    print(f"You'll need {cans} cans of paint.")


# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage) """

# ***************************************************************************

""" # 4.
# Write your code below this line 👇
def prime_checker(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print("It's not a prime number.")
                break
        else:
            print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n) """

# ***************************************************************************
alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# new_index = shifted_alphabet.index(l) + shift
# lst_text[lst_text.index(l)] = alphabet[new_index]

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encrypt(text, shift):
    lst_text = [l for l in text]
    shifted_alphabet = alphabet[shift:] + alphabet[0:shift]
    for l in range(len(lst_text)):
        a_index = alphabet.index(lst_text[l])
        lst_text[l] = shifted_alphabet[a_index]

    new_txt = "".join(lst_text)
    print(new_txt)


encrypt("civilization", 5)
