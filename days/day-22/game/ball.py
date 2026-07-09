# TODO - Create and move the paddle

from turtle import Turtle
import random

ROTATION = 250


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.set_random_heading()

    def move(self):
        self.forward(15)

    def paddle_bounce(self):
        # For vertical paddle bounces (left/right), flip the direction horizontally
        # new_heading = 180 - old_heading
        self.current_direction = 180 - self.current_direction
        self.setheading(self.current_direction)
        print(f"[PADDLE_BOUNCED]: {self.current_direction}")

    def wall_bounce(self):
        # For horizontal wall bounces (top/bottom), flip the direction vertically
        # new_heading = 360 - old_heading
        self.current_direction = 360 - self.current_direction
        self.setheading(self.current_direction)
        print(f"[WALL_BOUNCED]: {self.current_direction}")

    def set_random_heading(self):
        self.current_direction = random.randint(110, ROTATION)
        self.setheading(self.current_direction)

    def reset_position(self):
        self.goto(0, 0)
        self.set_random_heading()
