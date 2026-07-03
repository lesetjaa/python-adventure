from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
current_heading = 0

# TODO - Make Etch-a-sketch with the following commands
"""
W - Move forward
A - Rotate counter clockwise
S - Move backward
D - Rotate clockwise
C - Clear the screen and reset the turtle
"""


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def rotate_clockwise():
    global current_heading
    current_heading += 10
    tim.setheading(current_heading)


def rotate_counter_clockwise():
    global current_heading
    current_heading -= 10
    tim.setheading(current_heading)


def reset_turtle():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=reset_turtle)

screen.exitonclick()
