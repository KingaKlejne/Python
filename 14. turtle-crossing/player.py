from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def move_to_beginning(self):
        self.goto(STARTING_POSITION)
