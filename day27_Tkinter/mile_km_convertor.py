from tkinter import *


def button_clicked():
    pass


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def button_click():
    result = round(float(input.get()) * 1.609, 2)
    result_lable.config(text=result)


input = Entry(width=7)
input.insert(END, "0")
input.grid(column=1, row=0)

miles_lable = Label(text="Miles")
miles_lable.grid(column=2, row=0)

equal_lable = Label(text="is equal to")
equal_lable.grid(column=0, row=1)

result_lable = Label(text="0")
result_lable.grid(column=1, row=1)

km_lable = Label(text="Km")
km_lable.grid(column=2, row=1)

cal_button = Button(text="Calculate", command=button_click)
cal_button.grid(column=1, row=2)


window.mainloop()
