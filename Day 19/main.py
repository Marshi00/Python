import random
from turtle import Turtle, Screen
timmy = Turtle(shape="turtle")
timmy.penup()
screen = Screen()
screen.setup(width=500, height=400)
race_is_on = True
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle. color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)


while race_is_on and user_bet:
    for turtle in all_turtles:
        if turtle.xcor() < 230:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)
        else:
            race_is_on = False
            print(f"the winner is {turtle.pencolor()}")
            if user_bet == turtle.pencolor():
                print("you've won")
            else:
                print("you've lost")


screen.exitonclick()

