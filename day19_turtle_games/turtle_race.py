from turtle import Turtle, Screen
import random


def main():
    screen = Screen()
    screen.setup(width=500, height=400)
    screen.title("Welcome to the turtle race!")
    is_race_on = False
    user_bet = screen.textinput(
        title="Make your bet: ",
        prompt="Which turtle will win the race? Enter a color: ",
    ).lower()
    color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
    i = -100
    all_turtles = []
    for c in color_list:
        c_turtle = Turtle(shape="turtle")
        c_turtle.penup()
        c_turtle.goto(x=-230, y=i)
        c_turtle.color(c)
        all_turtles.append(c_turtle)
        i += 30

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

    screen.exitonclick()


if __name__ == "__main__":
    main()
