from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")
with open("data.txt") as file:
    contents = file.read()


class ScreenManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def update_screen(self, x, y, name):
        self.goto(x, y)
        self.write(f"{name}", align=ALIGNMENT, font=FONT)


class Scoreboard(ScreenManager):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as high_score_data:
            self.high_score = int(high_score_data.read())
        self.color("black")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.score = self.high_score
        with open("data.txt", mode="w") as high_score_data:
            high_score_data.write(f"\n{self.high_score}")
        self.score = 0
        self.update_scoreboard()

