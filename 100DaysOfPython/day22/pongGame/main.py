import turtle
from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
scoreboard = Scoreboard()

turtle.listen()
turtle.onkey(fun=r_paddle.move_up, key="Up")
turtle.onkey(fun=r_paddle.move_down, key="Down")
turtle.onkey(fun=l_paddle.move_up, key="w")
turtle.onkey(fun=l_paddle.move_down, key="s")


game_on = True
while game_on:
    time.sleep(ball.game_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    if ball.xcor() > 390:
        print("Right paddle missed!")
        ball.ball_reset()
        scoreboard.l_point()

    if ball.xcor() < -390:
        print("Left paddle missed!")
        ball.ball_reset()
        scoreboard.r_point()

screen.exitonclick()
