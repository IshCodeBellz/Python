from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.back(10)


def move_counter_clockwise():
    tim.right(10)


def move_clockwise():
    tim.left(10)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_counter_clockwise)
screen.onkey(key="a", fun=move_clockwise)
screen.onkey(key="c", fun=tim.reset)
screen.exitonclick()
