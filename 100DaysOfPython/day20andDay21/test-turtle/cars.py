from turtle import Turtle
import random

COLORS = ["yellow", "red", "blue", "purple", "green", "orange", "white"]
MOVE_DISTANCE = 5
SPEED_INCRE = 10


class Cars:
    def __init__(self):
        self.car_cart_storage = []
        self.car_speed = MOVE_DISTANCE

    def car_cart(self):
        dice = random.randint(1, 6)
        if dice == 1:
            cart = Turtle()
            cart.shape("square")
            cart.shapesize(stretch_wid=1, stretch_len=2)
            cart.color(random.choice(COLORS))
            cart.penup()
            y_axis = random.randint(-260, 260)
            cart.goto(280, y_axis)
            self.car_cart_storage.append(cart)

    def move_car_cart(self):
        for cars in self.car_cart_storage:
            cars.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += SPEED_INCRE
