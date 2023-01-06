# NOTE: Snake Game TODOs
# [x] TODO1: Create a snake body.
# [x] TODO2: How to move the snake.
# [x] TODO3: Control the snake body.
# [x] TODO4: Put the food on the screen, Detect collision with food & increase snake length as it eats food.
# [x] TODO5: Create a scoreboard & maintain it.
# [x] TODO6: Detect collision with walls.
# [x] TODO7: Detect collision with tail.

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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
    food = Food()
    score = Scoreboard()

    # To listen to key instruction from keyboard & control snake movement
    screen.listen()
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.left, key="Left")
    screen.onkey(fun=snake.right, key="Right")

    game_is_on = True
    while game_is_on:
        screen.update()  # it is necessary to call update after tracer method set to null.
        time.sleep(0.3)  # to control snake speed.
        snake.move()

        # Detect collision with food
        if snake.snake_head.distance(food) < 15:
            food.relocate()
            snake.extend()
            score.update_score()

        # Detect collision with wall
        if (
            snake.snake_head.xcor() > 280
            or snake.snake_head.xcor() < -280
            or snake.snake_head.ycor() > 280
            or snake.snake_head.ycor() < -280
        ):
            game_is_on = False
            [snake.clear() for snake in snake.snake_body]
            score.game_over()

        # Detect collision with tail.
        for part in snake.snake_body[1:]:
            if snake.snake_head.distance(part) < 10:
                game_is_on = False
                [snake.clear() for snake in snake.snake_body]
                score.game_over()
        # if head collides with tail, trigger game_over function

    screen.exitonclick()


if __name__ == "__main__":
    main()
