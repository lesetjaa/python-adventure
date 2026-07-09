# TODO - Create a scoreboard class that writes and updates the score on the screen

from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.goto((0, 280))
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.color("white")
        self.display_scoreboard()

    def player1_update_score(self):
        self.clear()
        self.player1_score += 1
        self.display_scoreboard()

    def player2_update_score(self):
        self.clear()
        self.player2_score += 1
        self.display_scoreboard()

    def display_scoreboard(self):
        self.write(f"{self.player1_score}   {self.player2_score}", align=ALIGNMENT, font=FONT)
