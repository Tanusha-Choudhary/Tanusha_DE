from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("black")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)
    def move_paddle(self):
        pass
    def up_paddle(self):
        self.y_pos=self.ycor() +20
        self.goto(self.xcor(), self.y_pos)
    def down_paddle(self):
        self.y_pos=self.ycor()-20
        self.goto(self.xcor(), self.y_pos)
    def right_paddle(self):
        self.x_pos=self.xcor()+20
        self.goto(self.x_pos, self.y_pos)
    def left_paddle(self):
        self.x_pos=self.xcor()-20
        self.goto(self.x_pos, self.y_pos)



