from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-20, 270)
        self.write(f"Score: {self.score}", font=(10))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", font=(10))

    def game_over(self):
        self.goto(-110, 0)
        self.clear()
        self.write(f"GAME OVER! Your score is: {self.score}", font=(10))
