from turtle import Turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
brick_range = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(colors))
        y_pos = random.randint(-250, 250)
        x_pos = random.randint(150, 300)
        self.goto(x_pos, y_pos)

    def moving_bricks(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())


