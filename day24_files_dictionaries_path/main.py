# [ ] TODO-1: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


starting_letter_path = (
    "./day24_files_dictionaries_path/Input/Letters/starting_letter.txt"
)
name_list_path = "./day24_files_dictionaries_path/Input/Names/invited_names.txt"
output_folder_path = "./day24_files_dictionaries_path/Output/ReadyToSend/"


letter = ""
names = []
with open(starting_letter_path, mode="r") as f:
    letter = f.read()

with open(name_list_path, mode="r") as f:
    for line in f.readlines():
        updated_line = line.strip("\n")
        names.append(updated_line)

for name in names:
    updated_letter = letter.replace("[name]", name)
    with open(output_folder_path + f"letter_for_{name}", mode="x") as f:
        f.write(updated_letter)
