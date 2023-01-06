from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """class to generate 3 snake instances & create basic snake body."""

    def __init__(self):
        """When called, this will display basic Snake body."""
        self.snake_body = []
        self.snake()
        self.snake_head = self.snake_body[0]
        self.snake_head.color("green")

    def snake(self):
        """default method to create snake body"""
        for position in STARTING_POSITIONS:
            self.add_body_part(position=position)

    def add_body_part(self, position):
        """Add a snake body part when asked

        Args:
            position (int): x-coordinate position
        """
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snake_body.append(snake)

    def extend(self):
        """Add new part at the tail of the snake"""
        self.add_body_part(self.snake_body[-1].position())

    def move(self):
        """when called, Snake will start moving in forward direction."""
        for index in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[index - 1].xcor()
            new_y = self.snake_body[index - 1].ycor()
            self.snake_body[index].goto(x=new_x, y=new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        """when called, Snake will turn 90°."""
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        """when called, Snake will turn 270°."""
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        """when called, Snake will turn 180°."""
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        """when called, Snake will turn 0°."""
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
