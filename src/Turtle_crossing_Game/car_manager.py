from turtle import Turtle

COLORS = ["red", "green", "blue", "yellow", "cyan", "magenta"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.hideturtle()
        self.score = 0
