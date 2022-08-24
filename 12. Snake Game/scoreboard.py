from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

with open("data.txt") as file:
    HIGH_SCORE = file.read()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(0, 275)
        self.color("white")
        self.score = 0
        self.high_score = int(HIGH_SCORE)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def new_score(self):
        self.score += 1
        self.update_scoreboard()

