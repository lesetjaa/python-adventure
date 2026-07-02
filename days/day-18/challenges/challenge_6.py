import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


for _ in range(72):
    current_heading = tim.heading()
    tim.seth(current_heading + 5)
    tim.color(random_color())
    tim.circle(100)

my_screen = t.Screen()
my_screen.exitonclick()
