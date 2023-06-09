from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over, your score is  {self.score}", align="center", font=("Arial", 12, "normal"))