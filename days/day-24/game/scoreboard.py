# TODO - Create a scoreboard class that writes and updates the score on the screen

from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')

# TODO - Read the highscore from data.txt


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.goto((0, 280))
        self.hideturtle()
        self.score = 0

        with open("data.txt") as data:
            self.highscore = int(data.read())

        self.color("white")
        self.display_scoreboard()

    def update_score(self):
        self.clear()
        self.display_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def display_scoreboard(self):
        self.write(
            f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto((0, 0))
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    # TODO - Write the new highscore to data.txt
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_score()
