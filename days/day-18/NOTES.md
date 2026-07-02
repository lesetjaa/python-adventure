# NOTES - Turtle and the Graphical User Interface (GUI)

## Turtle Module

The turtle module provides a simple graphics library for drawing shapes and patterns.

## Graphical User Interface

A visual way to offer interactions with a electronical device instead of typing on a keybord, we can just use a mouse and click to command the device

### Example: using turtle module

```python

from turtle import Turtle

my_turtle = Turtle()

# change the shape of the turtle
my_turtle.shape("turtle")

# change the color of the turtle
my_turtle.color("green")

# move the turtle and change the direction
my_turtle.forward(100)
my_turtle.right(60) # rotates 60 degrees to the right
```

### Changing the color mode

We need to tap into turtle itself to change the color mode inorder to make it easier to have actual random colors for the pen drawing

```python
import turtle as t # alias importing

t.colormode(255)
```

## Tuple

Another data type in python, looks similar to a list but it uses round brackets instead of square brackets

### Difference between tuple and a list

```python

my_tuple = (1, 3, 8)
my_list = [7, 3, 9]
```

- Unlike Lists, tuples are immutable (do not change)
- We cannot remove items from a tuple
