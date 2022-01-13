from turtle import Screen, Turtle
import time
from paddle import Pad
from ball import Ball
from scoreboard import Score

REFRESH_TIME = 0.06
speed = REFRESH_TIME

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

player1 = Pad(1)
player2 = Pad(2)
ball = Ball()
score = Score()

screen.listen()
screen.onkey(player1.go_up, "Up")
screen.onkey(player1.go_down, "Down")
screen.onkey(player2.go_up, "w")
screen.onkey(player2.go_down, "s")

game = True
right = True
left = True
while game:
    screen.update()
    time.sleep(speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(player1) < 50 and ball.xcor() > 320 and right:
        ball.bounce_x()
        if speed > 0.025: speed -= 0.005
        left = True
        right = False

    # Detect collision with l_paddle
    if ball.distance(player2) < 50 and ball.xcor() < -320 and left:
        ball.bounce_x()
        if speed > 0.025: speed -= 0.005
        left = False
        right = True

    # Detect when r misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_l_score()
        speed = REFRESH_TIME
        right = True
        left = True

    # Detect when l misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.increase_r_score()
        speed = REFRESH_TIME
        right = True
        left = True

screen.exitonclick()
