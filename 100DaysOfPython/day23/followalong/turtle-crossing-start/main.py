import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.moving_cars()

    for cars in car_manager.all_car:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.finish_line():
        player.go_to_starting_position()
        car_manager.level_up()
        scoreboard.level_up()

screen.exitonclick()
