from turtle import Turtle

MOVE_DISTANCE = 20


class TurtleAspects(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)
        self.color("black")

    def up(self):
        up_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), up_y)

    def down(self):
        down_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), down_y)
