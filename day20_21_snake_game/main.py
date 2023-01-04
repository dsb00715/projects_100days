# NOTE: Snake Game TODOs
# [x] TODO1: Create a snake body.
# [x] TODO2: How to move the snake.
# [x] TODO3: Control the snake body.
# [ ] TODO4: Put the food on the screen, Detect collision with food & increase snake length as it eats food.
# [ ] TODO5: Create a scoreboard & maintain it.
# [ ] TODO6: Detect collision with walls.
# [ ] TODO7: Detect collision with tail.

from turtle import Screen
from snake import Snake
import time


def main():
    """main loop that runs when program starts"""
    # Screen setup
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Welcome to Snake Game!")
    screen.tracer(0)

    # create instance from snake class to show snake body.
    snake = Snake()

    # To listen to key instruction from keyboard & control snake movement
    screen.listen()
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.left, key="Left")
    screen.onkey(fun=snake.right, key="Right")

    game_is_on = True
    while game_is_on:
        screen.update()  # it is necessary to call update after tracer method set to null.
        time.sleep(0.1)  # to control snake speed.
        snake.move()

    screen.exitonclick()


if __name__ == "__main__":
    main()
