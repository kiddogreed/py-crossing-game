from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("yellow")
        self.hideturtle()
        self.scores = 0
        self.write_score()

    def write_score(self):
        self.goto(-240, 265)
        self.write(f"Lvl={self.scores}", align="center", font=FONT)


    def scoring(self):
        self.clear()
        self.scores += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 265)
        self.clear()
        self.write(f"GAME OVER", align="center", font=FONT)

