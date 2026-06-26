# Move the turtle forward by 100 paces

from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("green")


my_screen = Screen()

my_turtle.forward(100)

my_screen.exitonclick()

