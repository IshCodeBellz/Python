import time
from turtle import Screen

from cars import Cars
from player import Player
from scoreboard import Scoreboard

MOVE_DISTANCE = 20

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


player = Player()
cars = Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.up, key="Up")
screen.onkey(fun=player.down, key="Down")
screen.onkey(fun=player.turn_left, key="Left")
screen.onkey(fun=player.turn_right, key="Right")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    cars.car_cart()
    cars.move_car_cart()

    for car in cars.car_cart_storage:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.start_point()
        scoreboard.level_up()
        cars.speed_up()


screen.exitonclick()
