import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("U.S States Game")
screen.bgcolor("black")
image ="1446677138_Find_the_US_States.png"
screen.addshape(image)
turtle.shape(image)
def get_mouse_click_coordinates(x,y):
    print(x,y)
turtle.onscreenclick(get_mouse_click_coordinates)
guessed_state=[]
df = pd.read_csv("50_state.csv")
all_state = df.state.to_list()
t1= turtle.Turtle()
t1.hideturtle()
t1.penup()
turtle.mainloop()

# screen.exitonclick()
# TODO: Also provide the coordinate if state is passed using csv
