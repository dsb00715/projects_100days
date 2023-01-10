from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
PADDLE_SPEED = "fastest"


class Player(Turtle):
    def __init__(self):
        """Creates player turtle"""
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.speed(PADDLE_SPEED)
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        """This method moves paddle in upward direction"""
        if self.ycor() < 260:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def reset_position(self):
        """Resets position of the player"""
        self.goto(STARTING_POSITION)
