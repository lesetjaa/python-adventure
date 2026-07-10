from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []

    def move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.setheading(180)
        car_x_pos = random.randint(300, 350)
        car_y_pos = random.randint(-250, 250)
        new_car.goto(car_x_pos, car_y_pos)
        self.cars.append(new_car)

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
