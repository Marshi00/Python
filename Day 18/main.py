import turtle
from turtle import Turtle, Screen
import random
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
direction = [0, 90, 180, 270]
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def dashed_move():
    for _ in range(5):
        timmy_the_turtle.pendown()
        timmy_the_turtle.forward(10)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(10)


def shape_move(angel, moves):
    for _ in range(moves):
        dashed_move()
        timmy_the_turtle.right(angel)


def draw_spirograph(gap):
    for _ in range(int(360/gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + gap)


draw_spirograph(5)
timmy_the_turtle.pensize(5)
timmy_the_turtle.setheading(random.choice(direction))
# movement = True
# while movement:
#     dashed_move()
#     timmy_the_turtle.setheading(random.choice(direction))
#     timmy_the_turtle.color(random_color())


# shape_move(120, 3)
# shape_move(90, 4)
# shape_move(72, 5)
# shape_move(60, 6)
# shape_move(45, 8)
# shape_move(40, 9)
# shape_move(36, 10)
