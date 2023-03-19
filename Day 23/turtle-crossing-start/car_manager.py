from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SCREEN_HEIGHT = (-300, 300)
SAFE_SPACE = 50
CAR_START_X = 320
CAR_SPAWN_SLOWDOWN = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_spawn_slowdown_counter = CAR_SPAWN_SLOWDOWN
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if self.car_spawn_slowdown_counter == 0:
            random_y = random.randint(SCREEN_HEIGHT[0] + SAFE_SPACE, SCREEN_HEIGHT[1] - SAFE_SPACE)
            new_car = Turtle(shape="square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(x=CAR_START_X, y=random_y)
            self.all_cars.append(new_car)
            self.car_spawn_slowdown_counter = CAR_SPAWN_SLOWDOWN
        else:
            self.car_spawn_slowdown_counter -= 1

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

