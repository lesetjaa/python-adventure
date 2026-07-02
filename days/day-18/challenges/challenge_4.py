from turtle import Turtle, Screen
import random

tur = Turtle()
tur.pensize(15)
tur.speed("fastest")
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
turn = ["forward", "back", "right", "left"]

for _ in range(50):
    color = random.choice(colors)
    direction = random.choice(turn)

    tur.color(color)

    match direction:
        case "back":
            tur.back(30)
        case "right":
            tur.right(90)
            tur.forward(30)
        case "left":
            tur.left(90)
            tur.forward(30)
        case "forward":
            tur.forward(30)


my_screen = Screen()
my_screen.exitonclick()
