from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("arrow")

colors = ["cyan", "aquamarine", "lime green", "dark green", "lawn green", "dark olive green", "yellow green",
          "teal", "dark khaki", "lawn green"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    # tim.color(random.choice(colors))
    randomNum = random.randint(0, 9)
    tim.color((colors[randomNum]))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()