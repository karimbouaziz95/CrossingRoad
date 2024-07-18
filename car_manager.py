from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.setheading(180)
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.initial_y = random.randint(-250, 250)
        self.goto(260, self.initial_y)
        self.color(random.choice(COLORS))

    def move(self):
        self.forward(MOVE_INCREMENT)
