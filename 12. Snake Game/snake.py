import turtle as t
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.squares = []
        self.create_object()
        self.head = self.squares[0]

    def create_object(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        object_created = t.Turtle(shape="square")
        object_created.color("white")
        object_created.penup()
        object_created.goto(position)
        self.squares.append(object_created)

    def extend(self):
        self.add_segment(self.squares[-1].position())

    def move(self):
        for square_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.squares[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.squares[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.squares[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.squares[0].setheading(RIGHT)


