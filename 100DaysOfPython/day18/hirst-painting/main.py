# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("hirst.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
x = -300
y = -420
tim.hideturtle()
tim.penup()
tim.goto(x, y)
tim.showturtle()


color_list = [(226, 231, 235), (54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62),
              (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122),
              (69, 101, 86), (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202),
              (232, 221, 225), (58, 47, 41), (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95),
              (118, 125, 145), (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52)]

for _ in range(10):
    y += 70
    tim.goto(x, y)
    for _ in range(10):
        tim.color(random.choice(color_list))
        tim.begin_fill()
        tim.circle(20)
        tim.end_fill()
        tim.penup()
        tim.forward(70)


screen = t.Screen()
screen.exitonclick()