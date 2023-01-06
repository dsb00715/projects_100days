from turtle import Turtle


PADDLE_SPEED = "fastest"
PADDLE_COLOR = "White"
# when up/down/w/s key is pressed, paddle will move for described steps here.
PADDLE_MOVE_DISTANCE = 20


class Paddle(Turtle):
    """this class is inherited from Turtle class and used for creating paddles in Pong game.

    Args:
        Turtle (_type_): Turtle library python.
    """

    def __init__(self, position, shape):

        """This method creates basic paddles of given shape on given position.

        Args:
            position (tuple): a location tuple is required.
            for ex., (350, 0)
            shape (str): required shape of the turtle.
            for ex., ("square")
        """
        super().__init__(shape=shape)
        self.color(PADDLE_COLOR)
        self.penup()
        self.speed(PADDLE_SPEED)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        """This method moves paddle in upward direction"""
        if self.ycor() < 260:
            self.goto(self.xcor(), self.ycor() + PADDLE_MOVE_DISTANCE)

    def down(self):
        """This method moves paddle in downward direction"""
        if self.ycor() > -260:
            self.goto(self.xcor(), self.ycor() - PADDLE_MOVE_DISTANCE)
