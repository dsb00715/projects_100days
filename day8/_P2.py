""" 
# Part1:

[x]TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

[x]TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
e.g.
plain_text = "hello"
shift = 5
cipher_text = "mjqqt"
print output: "The encoded text is mjqqt"

#HINT: How do you get the index of an item in a list:
https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

#🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

[x]TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. """

# ******************************************************************************************************************************************************************

""" 
# Part2:

[x]TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

[x]TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
e.g.
cipher_text = "mjqqt"
shift = 5
plain_text = "hello"
print output: "The decoded text is hello"


[x]TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. 
You should be able to test the code to encrypt *AND* decrypt a message. """


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

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    lst_text = [l for l in plain_text]
    shifted_alphabet = alphabet[shift_amount:] + alphabet[0:shift_amount]
    for l in range(len(lst_text)):
        a_index = alphabet.index(lst_text[l])
        lst_text[l] = shifted_alphabet[a_index]

    cipher_txt = "".join(lst_text)
    print(f"The encoded text is {cipher_txt}")


def decrypt(cipher_text, shift_amount):
    lst_text = [l for l in cipher_text]
    shifted_alphabet = alphabet[-shift_amount:] + alphabet[0:-shift_amount]
    for l in range(len(lst_text)):
        a_index = alphabet.index(lst_text[l])
        lst_text[l] = shifted_alphabet[a_index]

    plain_txt = "".join(lst_text)
    print(f"The decoded text is {plain_txt}")


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print("Please type eiher encode or decode! Anything else won't work")
