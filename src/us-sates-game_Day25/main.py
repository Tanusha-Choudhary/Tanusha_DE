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
while len(guessed_state) <50:
    answer_state = screen.textinput(f"{len(guessed_state)}/50 Guess the state","Whats another state  name")
    answer_state = answer_state.title()
    if  answer_state in all_state:
        guessed_state.append(answer_state)
        t1= turtle.Turtle()
        t1.hideturtle()
        t1.penup()
        state_cor = df[df.state == answer_state]
        # print(state_cor)
        t1.goto(state_cor.x.item(),state_cor.y.item())
        # print("Yes")
        t1.write(answer_state)
    elif answer_state.title() =="Exit" or answer_state.title() =="quit" :
        # missing_state =[]
        # for state in all_state:
        #     if state not in guessed_state:
        #         missing_state.append(state)
        missing_state = [ state for state in all_state if state not in guessed_state]
        print(missing_state)
        break

        print("No")
turtle.mainloop()

# screen.exitonclick()
# TODO: Also provide the coordinate if state is passed using csv
