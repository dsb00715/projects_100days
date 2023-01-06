from turtle import Turtle


class Scoreboard(Turtle):
    """This class is inherited from Turtle class and used for creating scoreboard.

    Args:
        Turtle (_type_): Turtle library python.
    """

    def __init__(self, position):
        """this method creates simple scoreboard.

        Args:
            position (tuple): a location tuple is required.
            for ex., (350, 0)
        """
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.write(f"Score: {self.score}", font=(10))

    def update_score(self):
        """This method updates scoreboard when called."""
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", font=(10))

    def game_over(self, side):
        self.goto(-120, 0)
        self.write(f"GAME OVER! {side} player wins", font=(10))
