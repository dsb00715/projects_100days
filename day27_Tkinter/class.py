# Tkinter basics

from tkinter import *


def button_clicked():
    my_label.config(text=input.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# Label
my_label = Label(text="My Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=100, y=200)  # specific places
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()  # starts with TOP Center
button.grid(column=1, row=1)

# test button
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# EntryBox
input = Entry(width=30)
input.insert(END, "Some text to begin with.")
# input.pack()
input.grid(column=3, row=2)

window.mainloop()


# unlimited (positional) arguments = *args
""" 
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(4, 5, 8)) 
"""

# unlimited keyword arguments = **kwargs
"""
def calculate(n, **kwargs):
    print(kwargs)  # {'add': 3, 'multiply': 5}
    print(type(kwargs))  # <class 'dict'>
    # for key, value in kwargs.items():
    #     print(key) # add
    #     print(value) # 3
    # print(kwargs["add"])  # 3
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)  # 2+3 * 5 = 25


calculate(2, add=3, multiply=5)
"""


""" class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model) """
