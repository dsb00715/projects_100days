from turtle import Turtle


class Snake:
    """class to generate 3 snake instances & create basic snake body"""

    def __init__(self):
        """_summary_"""
        self.snake_body = []
        self.x_cor = 0

        for _ in range(3):
            self.snake = Turtle(shape="square")
            self.snake.color("white")
            self.snake.penup()
            self.snake.goto(x=self.x_cor, y=0)
            self.snake_body.append(self.snake)
            self.x_cor -= 20

    def move(self):
        """when called, this function will keep moving snake in forward direction"""
        for index in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[index - 1].xcor()
            new_y = self.snake_body[index - 1].ycor()
            self.snake_body[index].goto(x=new_x, y=new_y)
        self.snake_body[0].forward(20)
