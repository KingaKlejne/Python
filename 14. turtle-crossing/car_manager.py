from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
WIDTH = 1
HEIGHT = 2

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_object(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            object_created = Turtle(shape="square")
            object_created.color(random.choice(COLORS))
            object_created.shapesize(WIDTH, HEIGHT)
            object_created.penup()
            object_created.setpos(300, random.randint(-250, 250))
            self.all_cars.append(object_created)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def move_faster(self):
        self.car_speed += MOVE_INCREMENT


