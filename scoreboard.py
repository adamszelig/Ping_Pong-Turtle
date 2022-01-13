from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 40, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 220)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 220)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.update_score()
