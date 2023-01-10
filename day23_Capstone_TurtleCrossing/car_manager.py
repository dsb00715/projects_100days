from turtle import Turtle
from random import choice, randrange, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []  # list of all the car object
        self.speed = 5

    def cars(self):
        """Creates multiple car(turtle) instances"""
        r = randint(1, 5)
        if r == 1:  # To decrease frequency of the cars
            turtle = Turtle("square")
            turtle.shapesize(stretch_wid=1, stretch_len=2)
            turtle.color(choice(COLORS))
            turtle.penup()
            turtle.goto(300, randrange(-250, 250, 5))
            self.all_cars.append(turtle)

    def move_cars(self):
        """Moves car instances from left to right"""
        for car in self.all_cars:
            car.goto(car.xcor() - self.speed, car.ycor())

    def increase_speed(self):
        """Increases games speed"""
        self.speed += 10
