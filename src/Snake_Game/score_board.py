from turtle import Turtle
ALIGNMENT = "right"
FONT = ("Courier", 18, "normal")
FONT = "arial"
from turtle import Screen
# S1=Screen()
# S1.setup(width=600,height=600)
# S1.bgcolor("black")
class ScoreBoard(Turtle):
    # score = 0
    def __init__(self):
        super().__init__()
        # self.high_score = 0
        self.score = 0
        with open("highest_score.txt", "r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("yellow")
        self.goto(0,270)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}: High scre: {self.high_score}", align=ALIGNMENT, font=(FONT, 18))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.color("red")

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highest_score.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

# S =ScoreBoard()
# S1.exitonclick()

