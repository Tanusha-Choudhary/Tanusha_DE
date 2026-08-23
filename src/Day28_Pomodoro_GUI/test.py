import time,math
from tkinter import *
YELLOW = "#E5D7BD"
FONT_NAME = "Courier"
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)

count = int(input("enter the number of minutes"))
count = count*60
canvas = Canvas(width=600, height=700,bg=YELLOW,highlightthickness=0)
img = PhotoImage(file="t.png")
canvas.create_image(250, 300, image=img)
timer_text = canvas.create_text(300,300,text="00:00", font=(FONT_NAME,75,"bold"))
canvas.grid(row=1, column=1)
while count >= 0:
    count_min = math.floor(count/60)
    count_sec = math.floor(count%60)
    # print(f"{count_min}:{count_sec}")
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    window.update()
    time.sleep(1)
    count = count - 1
window.mainloop()