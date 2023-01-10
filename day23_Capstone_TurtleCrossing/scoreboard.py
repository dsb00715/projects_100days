from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        """Creates scoreboard"""
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_level()

    def update_level(self):
        """displays scoreboard"""
        self.write(f"LEVEL:{self.level}", font=FONT)

    def increase_level(self):
        """Increases level on the scoreboard"""
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        """Game over sequence"""
        self.goto(-120, 0)
        self.write(f"GAME OVER!", font=FONT)
