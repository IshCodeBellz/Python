from turtle import Screen

from bricks import Bricks
from turtleaspects import TurtleAspects
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)


turtle_aspects = TurtleAspects()
for brick in range(0, 20):
    bricks = Bricks()
    bricks.moving_bricks()

screen.onkey(fun=turtle_aspects.up, key="Up")
screen.onkey(fun=turtle_aspects.down, key="Down")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()


screen.listen()
screen.exitonclick()
