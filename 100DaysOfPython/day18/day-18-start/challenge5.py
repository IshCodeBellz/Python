import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fast")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = tuple((r, g, b))
    return r_color


def draw_spirograph(gap):
    for _ in range(int(360/gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.tilt(5)
        tim.setheading(tim.heading() + 5)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()
