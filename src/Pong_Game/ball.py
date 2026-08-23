from turtle import Turtle
# from turtle import Screen
# import time
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# time.sleep(1)
# screen.title("Pong")
# screen.bgcolor()
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("circle")
        self.shapesize(1, 1)
        self.penup()
        self.move_speed = 0.1
        self.x_move=10
        self.y_move=10
    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    def bounce_y(self):
        self.y_move*=-1
        self.move_speed *= 0.9
        # self.forward(10)
    def bounce_x(self):
        self.x_move*=-1
        self.move_speed *= 0.9
        # self.forward(10)
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()






# ball=Ball()
# screen.exitonclick()
