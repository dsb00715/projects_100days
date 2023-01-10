from turtle import Turtle


FONT = ("Courier", 24, "normal")
FILE_PATH = ".\day20_21_snake_game\data.txt"


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open(FILE_PATH, mode="r") as f:
            self.high_score = int(f.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-200, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(FILE_PATH, mode="w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    """ def game_over(self):
        self.goto(-110, 0)
        self.clear()
        self.write(f"GAME OVER! Your score is: {self.score}", font=(10)) """
