# ---------------------------- REQUIRED MODULES ------------------------------- #
from tkinter import *
from tkinter import messagebox
from password_generator import create_password
from pyperclip import copy

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
LOGO_PATH = "./day29_Tkinter_PasswordGenerator/logo.png"
FILE_PATH = "./day29_Tkinter_PasswordGenerator/data.txt"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    password = create_password()
    password_entry.insert(0, password)
    copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def delete_info():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    note_entry.delete(0, END)


def add_info():
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showwarning(title="Oops!", message="Please fill in all the details!")
    else:
        is_ok = messagebox.askokcancel(
            title=website_entry.get(),
            message=f"You've entered following details: \nEmail: {email_entry.get()} \nPassword:{password_entry.get()} \nIs it ok to save?",
        )
        if is_ok:
            with open(FILE_PATH, "a") as f:
                f.writelines(
                    f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()} | {note_entry.get()}\n"
                )
                delete_info()
            messagebox.showinfo(
                title="Success!",
                message="Data successfully saved!",
            )


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file=LOGO_PATH)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website", font=(FONT_NAME, 10)).grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

email_label = Label(text="Email/Username", font=(FONT_NAME, 10)).grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.insert(0, "example@email.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

password_label = Label(text="Password", font=(FONT_NAME, 10)).grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")
password_button = Button(
    text="Generate Password", width=14, command=generate_password
).grid(row=3, column=2, columnspan=1, sticky="EW")

note_label = Label(text="Note", font=(FONT_NAME, 10)).grid(row=4, column=0)
note_entry = Entry(width=35)
note_entry.grid(row=4, column=1, columnspan=2, sticky="EW")

add_button = Button(text="Add", width=36, command=add_info).grid(
    row=5, column=1, columnspan=2, sticky="EW"
)

window.mainloop()
