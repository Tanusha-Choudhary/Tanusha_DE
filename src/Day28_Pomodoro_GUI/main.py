
# -------------------------- CONSTANTS ----------------
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#E5D7BD"
MUSTERD = "#decd87"
FONT_NAME = "Courier"

WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps=0
# ----------------------------- UI SETUP ----------------
from tkinter import *
import time
import math
timer = None
def reset_timer():
    global reps,timer
    if timer != None:
        window.after_cancel(timer)
        timer = None
    canvas.itemconfig(timer_text, text="00:00")
    label_title.config(text="Timer",bg=YELLOW,fg=GREEN)
    check_m.config(text="")
    reps = 0
def start_timer():
    global reps
    reps = reps + 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 ==0:
        count_down(long_break_sec)
        label_title.config(text="Long Break",bg=YELLOW,fg=GREEN)
    elif reps % 2 ==0:
        count_down(short_break_sec)
        label_title.config(text="Short Break",bg=YELLOW,fg=GREEN)
    else:
        count_down(work_sec)
        label_title.config(text="Work",bg=YELLOW,fg=GREEN)

def count_down(count):
    count_min = int(math.floor(count/60)) #roud to 4 minutes
    count_sec = int(math.floor(count%60)) # remainder
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}") #removed three line of code using :02d
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        mark = ""
        for i in range(math.floor(reps/2)):
            mark = mark + "☑️"
            check_m.config(text=mark)
        start_timer()
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)

start_button = Button(text="Start",font=(FONT_NAME,30),highlightthickness=0,command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset",highlightthickness=0,font=(FONT_NAME,30),command=reset_timer)
reset_button.grid(row=2, column=2)

label_title = Label(text="TIMER", bg=YELLOW,fg=GREEN,font=(FONT_NAME,30))
label_title.grid(row=0, column=1)

check_m =Label(text="",fg=GREEN,bg=YELLOW,font=(FONT_NAME,40))
check_m.grid(row=3, column=1)

canvas = Canvas(width=600, height=700,bg=YELLOW,highlightthickness=0)
img = PhotoImage(file="t.png")

canvas.create_image(250, 300, image=img)
timer_text = canvas.create_text(300,300,text="00:00", font=(FONT_NAME,75,"bold"))
# count_down(5)
canvas.grid(row=1,column=1)

window.mainloop()
