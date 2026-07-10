import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
screen.listen()
screen.onkeypress(fun=turtle.move_up, key="Up")

cars = CarManager()
scoreboard = Scoreboard()

car_creation_chance = 0 # 

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    if car_creation_chance > 5:
        cars.create_car()
        car_creation_chance = 0
    cars.move()
    car_creation_chance += 1

    # Detect collision with car
    for car in cars.cars:
        if car.distance(turtle) < 22:
            scoreboard.game_over()
            game_is_on = False

    # Detect finish line cross
    if turtle.ycor() > 290:
        scoreboard.update_level()
        turtle.reposition()
        cars.increase_speed()

screen.exitonclick()