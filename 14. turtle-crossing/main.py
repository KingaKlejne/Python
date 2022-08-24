import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move_forward)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_object()
    car_manager.move_cars()

    # Detect successful crossing
    if player.ycor() > 280:
        player.move_to_beginning()
        scoreboard.new_level()
        car_manager.move_faster()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 15:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()