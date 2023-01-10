# Update Snake Project with HighScore feature

""" 
file = open(".\day24_files_dictionaries_path\my_file.txt")
content = file.read()
print(content)
file.close() 
"""


FILE_PATH = "./day24_files_dictionaries_path/my_file.txt"

with open(FILE_PATH, mode="r") as f:
    # f.write("\nNew Text.")
    print(f.read())
