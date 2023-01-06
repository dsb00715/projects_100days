from turtle import Turtle


BALL_COLOR = "White"


class Ball(Turtle):
    """This class is inherited from Turtle class and used for creating & moving ball.

    Args:
        Turtle (_type_): Turtle library python.
    """

    def __init__(self):
        """this method creates simple ball on default location(0,0)."""
        super().__init__()
        self.shape("circle")
        self.color(BALL_COLOR)
        self.penup()
        self.x_cor = 10
        self.y_cor = 10
        self.move_speed = 0.1

    def move(self):
        """this method moves ball towards top right corner from default location(0,0)."""
        self.goto(self.xcor() + self.x_cor, self.ycor() + self.y_cor)

    def bounce(self):
        """this method bounces ball when it touches upper & lower walls."""
        self.y_cor *= -1

    def paddle_bounce(self):
        """This method bounces the ball when it touches any paddle."""
        self.x_cor *= -1
        self.move_speed *= 0.9

    def reset(self):
        """This method resets the ball position & direction when it misses the paddle on left/right side."""
        self.goto(0, 0)
        self.x_cor *= -1
        self.move_speed = 0.1
