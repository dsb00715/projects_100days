"""
# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
"""

from alphabets import alphabet_t, alphabet

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

""" # my style - if you want to run this: Please import alphabet instead of alphabet_t
def caesar(start_text, shift_amount, direction):
    lst_text = [l for l in start_text]
    if direction == "encode":
        shifted_alphabet = alphabet[shift_amount:] + alphabet[0:shift_amount]
    elif direction == "decode":
        shifted_alphabet = alphabet[-shift_amount:] + alphabet[0:-shift_amount]
    for index in range(len(lst_text)):
        alphabet_index = alphabet.index(lst_text[index])
        lst_text[index] = shifted_alphabet[alphabet_index]
    final_text = "".join(lst_text)
    print(f"The {direction}d text is {final_text}") """


def caesar(start_text, shift_amount, direction):
    final_text = ""
    for letter in start_text:
        position = alphabet_t.index(letter)
        if direction == "encode":
            new_position = position + shift_amount
        else:
            new_position = position - shift_amount
        final_text += alphabet_t[new_position]
    print(f"The {direction}d text is {final_text}")


if direction == "encode" or direction == "decode":
    caesar(start_text=text, shift_amount=shift, direction=direction)
else:
    print("Please insert either 'encode' or 'decode'. Anything else won't work!")
