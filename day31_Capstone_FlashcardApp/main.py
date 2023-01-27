# ---------------------------- REQUIRED MODULES ------------------------------- #
from tkinter import *
import pandas as pd
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
BACK_IMAGE = "day30_Capstone_FlashcardApp\images\card_back.png"
FRONT_IMAGE = "day30_Capstone_FlashcardApp\images\card_front.png"
RIGHT_IMAGE = "./day30_Capstone_FlashcardApp/images/right.png"
WRONG_IMAGE = "day30_Capstone_FlashcardApp\images\wrong.png"
MAIN_FILE = "day30_Capstone_FlashcardApp\data\german_words.csv"
WORDS_TO_LEARN = "day30_Capstone_FlashcardApp\data\words_to_learn.csv"
card_data = {}

try:
    data_df = pd.read_csv(WORDS_TO_LEARN, encoding="ISO-8859-1")
except FileNotFoundError:
    data_df = pd.read_csv(MAIN_FILE, encoding="ISO-8859-1")
finally:
    data = data_df.to_dict(orient="records")

# ---------------------------- Timer function ------------------------------- #
def flip_card():
    global card_data
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(language_label, text="English", fill="White")
    canvas.itemconfig(word_label, text=card_data["English"], fill="White")


# ---------------------------- Update list ------------------------------- #
def update_list():
    global card_data, data
    data.remove(card_data)
    final_df = pd.DataFrame(data)
    final_df.to_csv(WORDS_TO_LEARN, encoding="ISO-8859-1", index=False)
    create_card()


# ---------------------------- Create Flash Cards ------------------------------- #
def create_card():
    global card_data, flip_timer
    window.after_cancel(flip_timer)
    card_data = random.choice(data)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(language_label, text="German", fill="Black")
    canvas.itemconfig(word_label, text=card_data["German"], fill="Black")
    flip_timer = window.after(5000, func=flip_card)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

flip_timer = window.after(5000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file=FRONT_IMAGE)
back_image = PhotoImage(file=BACK_IMAGE)
canvas_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)

language_label = canvas.create_text(
    400, 150, text="Title", fill="black", font=LANGUAGE_FONT
)
word_label = canvas.create_text(400, 263, text="Word", fill="black", font=WORD_FONT)

wrong_image = PhotoImage(file=WRONG_IMAGE)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=create_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file=RIGHT_IMAGE)
right_button = Button(image=right_image, highlightthickness=0, command=update_list)
right_button.grid(row=1, column=1)

create_card()
window.mainloop()
