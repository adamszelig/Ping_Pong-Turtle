from turtle import Turtle
INIT1_POS = (350, 0)
INIT2_POS = (-350, 0)
MOVESENS = 40


class Pad(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        if position == 1:
            self.goto(INIT1_POS)
        if position == 2:
            self.goto(INIT2_POS)

    def go_up(self):
        if self.ycor() < 250 - MOVESENS:
            new_y = self.ycor() + MOVESENS
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -250 + MOVESENS:
            new_y = self.ycor() - MOVESENS
            self.goto(self.xcor(), new_y)
