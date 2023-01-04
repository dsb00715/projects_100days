from turtle import Turtle, Screen
import random


def main():
    # Screen setup
    screen = Screen()
    screen.setup(width=500, height=400)
    screen.title("Welcome to the turtle race!")

    is_race_on = False  # this decides when to start/end race.
    # to get user input from popup
    user_bet = screen.textinput(
        title="Make your bet: ",
        prompt="Which turtle will win the race? Enter a color: ",
    ).lower()
    color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
    i = -100
    all_turtles = []
    for c in color_list:
        """This loop generates all different turtle objects"""
        c_turtle = Turtle(shape="turtle")
        c_turtle.penup()
        c_turtle.goto(x=-230, y=i)
        c_turtle.color(c)
        all_turtles.append(c_turtle)  # to get all the turtles
        i += 30

    if user_bet:
        is_race_on = True

    while is_race_on:
        """This loop repeats to move turtles forward."""
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False  # this stops the loop
                winning_color = turtle.pencolor()  # to get the winning color
                [t.reset() for t in all_turtles]  # removes all turtles from the screen
                # Present the winning turtle in the middle of the screen with increased size
                turtle.goto(x=0, y=0)
                turtle.color(winning_color)
                turtle.turtlesize(stretch_wid=5, stretch_len=5, outline=8)

                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
            # increases distance for particular turtle each time
            turtle.forward(random.randint(0, 10))

    screen.exitonclick()


if __name__ == "__main__":
    main()
