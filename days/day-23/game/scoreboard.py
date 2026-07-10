from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-220, 250)
        self.hideturtle()
        self.level = 0
        self.display_score()

    def display_score(self):
        self.write(f"Level: {self.level}", font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.display_score()

    def game_over(self):
        self.goto((0, 0))
        self.write("Game Over", align="center", font=FONT)