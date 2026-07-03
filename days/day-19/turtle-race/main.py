from turtle import Turtle, Screen
import random

# tim = Turtle(shape="turtle")
is_race_on = False
screen = Screen()
colors = ["red", "yellow", "orange", "green", "blue", "purple"]

# setting the width and height of the screen
screen.setup(width=500, height=400)

# Prompt the user for their bet selection
user_bet = screen.textinput("Make Your Bet", "Which turtle will win the race?")
turtles_list = []

# Move the turtle to the starting point
# tim.penup()
# tim.goto(x=-240, y=-100)


# TODO - Create 6 turtles and move them to their starting points
y_coord = -100
for turtle_num in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_num])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_coord)
    y_coord += 50
    turtles_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles_list:

        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()

            if user_bet == winning_color:
                print("You've won! The {winning_color} turtle is the winner!")
            else:
                print("You've lost! The {winning_color} turtle is the winner!")
            is_race_on = False
            break
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
