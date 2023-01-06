from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
LEFT_POSITION = (-350, 0)
RIGHT_POSITION = (350, 0)
LEFT_SCORE = (-200, 260)
RIGHT_SCORE = (200, 260)

# Basic screen settings
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Welcome to Pong Game!")
screen.bgcolor("black")
screen.tracer(0)  # to remove animation

# create left & right paddle
left_paddle = Paddle(position=LEFT_POSITION, shape="square")
right_paddle = Paddle(position=RIGHT_POSITION, shape="square")

# create ball
ball = Ball()

# create scoreboards for both players
left_score = Scoreboard(position=LEFT_SCORE)
right_score = Scoreboard(position=RIGHT_SCORE)

# to move left & right paddles up or down based on key-press
screen.listen()
screen.onkeypress(fun=left_paddle.up, key="w")
screen.onkeypress(fun=left_paddle.down, key="s")
screen.onkeypress(fun=right_paddle.up, key="Up")
screen.onkeypress(fun=right_paddle.down, key="Down")

game_is_on = True
while game_is_on:
    """This loop will run forever until game_is_on is False or user closes the window."""
    time.sleep(ball.move_speed)  # to pause the loop for 0.1 second
    screen.update()  # because tracer method is used above!
    ball.move()
    # Detect collision with the upper & lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # Detect collision with left & right paddle
    if (ball.distance(left_paddle) < 50 and ball.xcor() < -320) or (
        ball.distance(right_paddle) < 50 and ball.xcor() > 320
    ):
        ball.paddle_bounce()

    # Detect collision with left & Right wall, if paddle misses
    if ball.xcor() > 380:
        ball.reset()
        left_score.update_score()
    elif ball.xcor() < -380:
        ball.reset()
        right_score.update_score()

    # Detect game over scenario
    if left_score.score > 9:
        game_is_on = False
        left_score.game_over("left")

    elif right_score.score > 9:
        game_is_on = False
        right_score.game_over("right")


screen.exitonclick()
