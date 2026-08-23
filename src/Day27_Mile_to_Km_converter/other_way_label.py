import tkinter as tk
window = tk.Tk()
window.title("My First GUI")
window.minsize(width=300, height=300)

# LABEL #Button
my_label=tk.Label(text="I am a label",font=("Arial", 18,"bold"),bg="blue",fg="black")
# or # my_label["fg"] = "black"
# or # my_label.config(fg="black")
my_label.pack(side="bottom")
# my_label["text"] = "My first GUI FOR YOU <3"
# OR
my_label.config(text="My first GUI FOR YOU <3")




window.mainloop()