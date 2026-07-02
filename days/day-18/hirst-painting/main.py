import turtle as t
import random
# import colorgram

# colors = colorgram.extract('hirst-painting/image.jpg', 30)
# for color in colors:
#     r = color.r
#     g = color.g
#     b = color.b
#     new_color = (r, g, b)
#     color_list.append(new_color)


color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

# configure the turtle
tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.hideturtle()


def draw_row():

    for _ in range(10):
        tim.penup()
        tim.dot(20, random.choice(color_list))
        tim.forward(50)


def reposition_turtle():

    current_position = tim.position()
    x_pos = current_position[0]

    tim.penup()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(x_pos)
    tim.setheading(0)


for _ in range(10):
    draw_row()
    reposition_turtle()


turtle_screen = t.Screen()
turtle_screen.exitonclick()
