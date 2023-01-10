import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

# Screen configuration
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Player configuration
player = Player()

# Car management configuration
car_manager = CarManager()

# scoreboard initialization
score = Scoreboard()


# To move player(turtle) in upward direction
screen.listen()
screen.onkeypress(fun=player.up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.cars()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False

    # Detect level up
    if player.ycor() > 259:
        player.reset_position()
        car_manager.increase_speed()
        score.increase_level()


screen.exitonclick()
