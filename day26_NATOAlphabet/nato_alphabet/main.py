import pandas as pd

# [x] TODO-1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
FILE_PATH = "day26_NATOAlphabet/nato_alphabet/nato_phonetic_alphabet.csv"
data = pd.read_csv(FILE_PATH)
nato_dict = {row["letter"]: row["code"] for i, row in data.iterrows()}


# [x] TODO-2. Create a list of the phonetic code words from a word that the user inputs.
should_continue = True
while should_continue:
    try:
        user_word = input("Enter a word: ").upper()
        nato_list = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
    else:
        print(nato_list)
        should_continue = False
