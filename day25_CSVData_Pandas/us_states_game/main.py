""" # to get co-ordinates of a click place
def get_mouse_click_cor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_cor)

turtle.mainloop() """

import turtle
import pandas as pd


IMAGE = "day25_CSVData_Pandas/us_states_game/blank_states_img.gif"
CSV_FILE = "day25_CSVData_Pandas/us_states_game/50_states.csv"

# Screen Configuration
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

state = turtle.Turtle()
state.penup()
state.hideturtle()

# create DataFrame
data = pd.read_csv(CSV_FILE)
all_states = data["state"].to_list()
count = 0
guessed_list = []
remaining_states = []

while count < 50:
    # To get user guess recorded
    guess = screen.textinput(
        f"{count}/50 States Correct", prompt="what's another states's name?"
    ).title()

    if guess == "Exit":
        remaining_states = [
            state for state in all_states if state not in guessed_list
        ]  # list comprehension
        remaining_states_df = pd.DataFrame(remaining_states, columns=["state"])
        remaining_states_df.to_csv(
            "day25_CSVData_Pandas/us_states_game/states_to_learn.csv"
        )
        break

    for index, row in data.iterrows():
        # this loop iterates through whole dataset. & below line checks if user has guessed correct state.
        if row["state"] == guess:
            state.goto(row["x"], row["y"])
            state.write(row["state"])
            guessed_list.append(row["state"])
            count += 1
