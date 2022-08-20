from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(0, 275)
        self.color("white")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def new_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

