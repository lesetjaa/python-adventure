from turtle import Turtle

snake_body_coord = 0
distance = 20


class Snake:

    # TODO - Create the snake and its body, placing them in the correct place
    # Snake Setup
    def __init__(self) -> None:
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def move(self):
        """ Here is how the snake moves: 
            - We take the body part from behind and move it to where the next body part is
            - We control the head's movement because the rest of the body parts will follow
        """
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)

        self.snake[0].forward(distance)

    def create_snake(self):
        global snake_body_coord
        for _ in range(3):
            snake_part = Turtle(shape="square")
            snake_part.speed("slowest")
            snake_part.penup()
            snake_part.color("white")
            snake_part.goto(x=snake_body_coord, y=0)
            snake_body_coord -= 20
            self.snake.append(snake_part)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
