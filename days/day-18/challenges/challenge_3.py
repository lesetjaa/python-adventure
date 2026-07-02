# TODO - Draw shapes

from turtle import Turtle, Screen

# tur = Turtle()

# angle = 360 / 5
# for _ in range(5):
#     tur.right(angle)
#     tur.forward(100)


# my_screen = Screen()
# my_screen.exitonclick()

# Solution

jim = Turtle()


def draw_shape(num_sides):
    angle = 360 / num_sides

    for _ in range(num_sides):
        jim.forward(100)
        jim.right(angle)


for _ in range(20000, 2000000):
    draw_shape(_)
