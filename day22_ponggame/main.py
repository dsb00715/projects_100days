from turtle import Screen, Turtle
from paddles import Paddle
import time

LEFT_POSITION = (-350, 0)
RIGHT_POSITION = (350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Welcome to Pong Game!")
screen.bgcolor("black")
screen.tracer(0)

left_paddle = Paddle(LEFT_POSITION)
right_paddle = Paddle(RIGHT_POSITION)

screen.listen()
screen.onkeypress(fun=left_paddle.up, key="w")
screen.onkeypress(fun=left_paddle.down, key="s")
screen.onkeypress(fun=right_paddle.up, key="Up")
screen.onkeypress(fun=right_paddle.down, key="Down")

game_is_on = True
while game_is_on:
    screen.update()
    # time.sleep(0.1)


screen.exitonclick()
