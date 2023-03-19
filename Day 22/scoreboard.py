from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(x=-100, y=200)
        self.write(f"Score: {self.l_score}", align="center", font=("Arial", 12, "normal"))
        self.goto(x=100, y=200)
        self.write(f"Score: {self.r_score}", align="center", font=("Arial", 12, "normal"))

    def increase_score(self, side):
        if side == "r":
            self.r_score += 1
        elif side == "l":
            self.l_score += 1
        self.clear()
        self.update_scoreboard()

