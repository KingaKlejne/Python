from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(-230, 275)
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level = {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def new_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
