from turtle import Turtle, Screen
from snake import Snake
import random
import time


def main():
    """main loop that runs when program starts"""
    # Screen setup
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Welcome to Snake Game!")
    screen.tracer(0)

    snake = Snake()

    """ # functional way of creating snake body
    snake_body = []
    x_cor = 0
    for _ in range(3):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(x=x_cor, y=0)
        snake_body.append(snake)
        x_cor -= 20 """

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.5)
        """ # functional way of coding move method 
        for index in range(len(snake_body) - 1, 0, -1):
            new_x = snake_body[index - 1].xcor()
            new_y = snake_body[index - 1].ycor()
            snake_body[index].goto(x=new_x, y=new_y)
        snake_body[0].forward(20) """
        snake.move()

    screen.exitonclick()


if __name__ == "__main__":
    main()
