# TODO - Create a scoreboard class that writes and updates the score on the screen

from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.goto((0, 280))
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.display_scoreboard()

    def update_score(self):
        self.clear()
        self.score += 1
        self.display_scoreboard()

    def display_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto((0, 0))
        self.write("Game Over", align=ALIGNMENT, font=FONT)
