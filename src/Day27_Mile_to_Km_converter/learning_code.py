from tkinter import *

#Button
def button_clicked():
    print("I got clicked")
    answer =input.get()
    my_label.config(text=answer)

# window
window = Tk()
window.title("My First GUI")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

# LABEL
my_label=Label(text="I am a label",font=("Arial", 18,"bold"),bg="blue",fg="black")
my_label.config(text="New text")
# my_label.pack(side="top")
# my_label.place(x=100,y=200)
my_label.grid(row=0,column=0)
# Button
button = Button(text="Click Me",command=button_clicked)
button.grid(row=2,column=1)

button1 = Button(text="History",command=button_clicked)
button1.grid(row=1,column=2)
# button.pack()
# ENTRY
input = Entry(width=10)
input.grid(row=3,column=3)
# input.pack()





window.mainloop()