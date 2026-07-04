# Notes - Snake Game Part 1

## Animations

When we command a turtle to go to a place there is some animation it does between its current position to the next position

- We can remove the animation and tell the screen when to update the screen

```python
from turtle import Screen, Turtle

screen = Screen()

# Here we turn of the animations of the screen
screen.tracer(0) # Nothiong will show when we run the screen at this point

""" Code to draw the snake """

""" In between the loop for moving the snake """
screen.update()
```
