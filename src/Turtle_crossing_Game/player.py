from turtle import Turtle

STARTING_POSITION = (0,-280)
MoVE_DISTANCE = 10
FINISH_DISTANCE = 280
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")