import turtle as t
import random

tim = t.Turtle()
tim.shape("arrow")
tim.width(15)
tim.speed("fastest")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = tuple((r, g, b))
    return r_color


# colors = ['red', 'orange', 'yellow', 'green', 'blue',
#           'purple', 'pink', 'brown', 'gray', 'gold', 'cyan', 'Gainsboro', 'gray',
#           'dimgray', 'LightSlateGray', 'AliceBlue', 'LimeGreen', 'DarkKhaki', 'Khaki']


directions = [0, 90, 180, 270]
motions = [30, -30]

for _ in range(0, 1001):
    colours = random_color()
    tim.color(colours)
    print(colours)
    tim.forward(random.choice(motions))
    tim.right(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
