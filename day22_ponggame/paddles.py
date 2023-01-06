from turtle import Turtle


UP = 90
DOWN = 180


class Paddle:
    def __init__(self, position):
        self.paddle = self.create_paddle(position)

    def create_paddle(self, position):
        paddle = Turtle("square")
        paddle.color("white")
        paddle.penup()
        paddle.speed(0)
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.goto(position)

        return paddle

    def up(self):
        # self.y_cor += 20
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + 20)

    def down(self):
        # self.y_cor -= 20
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - 20)
