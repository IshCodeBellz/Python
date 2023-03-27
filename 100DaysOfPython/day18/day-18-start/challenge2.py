from turtle import Turtle, Screen
# import turtle as t
# tim = t.Turtle()

tim = Turtle()
tim.shape("arrow")
tim.color("black")

for _ in range(30):
    tim.pendown()
    tim.forward(5)
    tim.penup()
    tim.forward(5)


screen = Screen()
screen.exitonclick()