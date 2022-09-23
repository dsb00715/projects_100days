""" 
#TODO-1: Import and print the logo from art.py when the program starts.

TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
Try running the program and entering a shift number of 45.
Add some code so that the program continues to work even if the user enters a shift number greater than 26.
Hint: Think about how you can use the modulus (%).

TODO-3: What happens if the user enters a number/symbol/space?
Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
e.g. start_text = "meet me at 3"
end_text = "•••• •• •• 3"

TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
"""
from art import logo
from alphabets import alphabet_t, alphabet


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        """ """
        if letter not in alphabet_t:
            end_text += letter
        else:
            position = alphabet_t.index(letter)
            new_position = position + shift_amount
            end_text += alphabet_t[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}")


def caesar1(start_text, shift_amount, cipher_direction):
    lst_text = [l for l in start_text]
    if cipher_direction == "encode":
        shifted_alphabet = alphabet[shift_amount:] + alphabet[0:shift_amount]
    elif cipher_direction == "decode":
        shifted_alphabet = alphabet[-shift_amount:] + alphabet[0:-shift_amount]
    for index in range(len(lst_text)):
        if lst_text[index] in alphabet:
            alphabet_index = alphabet.index(lst_text[index])
            lst_text[index] = shifted_alphabet[alphabet_index]
    final_text = "".join(lst_text)
    print(f"The {direction}d text is {final_text}")


re_run = True

while re_run:

    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if shift > 26:
            shift = shift % 26

        # Enable either caesar or caesar1

        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
        # caesar1(start_text=text, shift_amount=shift, cipher_direction=direction)
    else:
        print("Please insert either 'encode' or 'decode'. Anything else won't work!")
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart != "yes":
        break
