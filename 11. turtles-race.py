import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_list = [x for x in range(-150, 200, 50)]
turtles = []


def create_turtle(turtle_color):
    turtle = t.Turtle(shape="turtle")
    turtle.color(turtle_color)
    return turtle

def set_position(turtle, y_line, x_line = -200):
    turtle.penup()
    turtle.setpos(x_line, y_line)


for i in range(6):
    turtle = create_turtle(colors[i])
    set_position(turtle,int(y_list[i]))
    turtles.append(turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()