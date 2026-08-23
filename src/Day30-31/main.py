from tkinter import *
import random
import pandas
import time
from PIL import Image, ImageTk, ImageOps

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("2000Dutch.txt", sep="\t",index=False)

to_learn = data.to_dict(orient="records")
random_word = random.choice(to_learn)
current_card = {}
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_title,text="Dutch",fill="black")
    canvas.itemconfig(canvas_word,text=current_card["Dutch"],fill="black")
    # canvas.itemconfig(canvas_bk,img=back_mg)
    flip_timer = window.after(3000,func=flip_the_card)

def flip_the_card():
    canvas.itemconfig(canvas_title,text="English",fill="green")
    canvas.itemconfig(canvas_word,text=current_card["English"],fill="green")

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    pandas.DataFrame(to_learn).to_csv("words_to_learn.csv",index=False)
    next_card()
    # print(to_learn)
window = Tk()
window.title("Wordlist")
window.config(padx=50,pady=50,bg="#B1DDC6")
flip_timer = window.after(3000,func=flip_the_card)
img = Image.open("Title1.png")
img = img.resize((320,320))
img = ImageOps.expand(img, border=10, fill="white")
front_mg = ImageTk.PhotoImage(img)
back_mg = ImageTk.PhotoImage(img)

canvas = Canvas(window,width=480, height=320, bg="white",highlightthickness=0)
canvas_bk = canvas.create_image(240,160,image=front_mg)
canvas_title= canvas.create_text(240,120,text="Title",font=("Ariel",30,"bold"),fill="black")
canvas_word=canvas.create_text(240,160,text="WORD",font=("Ariel",50,"bold"),fill="green")
canvas.grid(row=0,column=0,columnspan=2)
Button1= Button(window, text="☑️",borderwidth=0,bg="#B1DDC6",highlightthickness=0,command=is_known)
Button1.grid(row=1,column=0)
Button2= Button(window, text="️❎",borderwidth=0,fg="green",bg="#B1DDC6",highlightthickness=0,command=next_card)
Button2.grid(row=1,column=1)
next_card()
window.mainloop()