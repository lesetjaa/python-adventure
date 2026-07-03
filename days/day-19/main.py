from turtle import Turtle, Screen

tim = Turtle()
tim.speed('fastest')
my_screen = Screen()


def move_forward():
    tim.forward(10)


my_screen.listen()
my_screen.onkey(fun=move_forward, key="w")

my_screen.exitonclick()
