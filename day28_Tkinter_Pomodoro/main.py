# ---------------------------- REQUIRED MODULES ------------------------------- #
from tkinter import *
import tkinter.messagebox

# import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global timer

    start_button.config(state="normal")
    reset_button.config(state="disabled")

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_lable.config(text="Timer", fg=GREEN)
    check_mark_lable.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    start_button.config(state="disabled")
    reset_button.config(state="normal")

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        tkinter.messagebox.showinfo(title="Work", message="Let's Focus on Work!")
        count_down(work_sec)
        timer_lable.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        tkinter.messagebox.showinfo(title="Break", message="Take a long break now!")
        count_down(long_break_sec)
        timer_lable.config(text="Break", fg=RED)
    else:
        tkinter.messagebox.showinfo(title="Work", message="Take a small break!")
        count_down(short_break_sec)
        timer_lable.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global timer
    # count_min = math.floor(count / 60)
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check = ""
        for _ in range(reps // 2):
            check += CHECK_MARK
        check_mark_lable.config(text=check)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Application")
window.config(padx=100, pady=50, bg=YELLOW)

timer_lable = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
timer_lable.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./day28_Tkinter_Pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold")
)
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark_lable = Label(font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW)
check_mark_lable.grid(column=1, row=3)

window.mainloop()
