from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=800, width=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle = Paddle((-380, 0))
computer_paddle = Paddle((380, 0))
scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(key="Up", fun=paddle.up)
screen.onkey(key="Down", fun=paddle.down)

screen.onkey(key="w", fun=computer_paddle.up)
screen.onkey(key="s", fun=computer_paddle.down)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    ball.move()

    # detect collison with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # detect collision with paddles
    if ball.distance(paddle) < 50 or ball.distance(computer_paddle) < 50:
        ball.paddle_bounce()

    # detect poddle miss
    if ball.xcor() < -400:
        scoreboard.player2_update_score()
        ball.reset_position()

    if ball.xcor() > 400:
        scoreboard.player1_update_score()
        ball.reset_position()

screen.exitonclick()
