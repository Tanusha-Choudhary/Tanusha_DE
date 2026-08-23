#window
from tkinter import *
import requests
from PIL import Image, ImageTk, ImageOps # Added for resizing
from docutils.nodes import label

YELLOW = "#E5D7BD"
#canvas
def get_quote():
    response = requests.get("https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json()["quote"]
    quote_label.config(text=data)
window = Tk()
window.title("kanye Quotes")
window.config(padx=10,pady=10)
img = Image.open("cart.png").resize((320,320))
img = ImageTk.PhotoImage(img)
# img = PhotoImage(file="cart.png")
canvas=Canvas(width=500, height=500,bg=YELLOW,highlightthickness=0)
canvas.create_image(250, 250, image=img)
quote_text= canvas.create_text(250,250,text="Kanye Quote",width=250,
    font=("Arial", 16, "italic"), fill="white")
button = Button(text="New Quote", command=get_quote)
button.grid(row=3, column=1)
quote_label = Label(
    text="Quote will appear here",
    wraplength=400,
    font=("Arial", 14, "italic")
)
quote_label.grid(row=2, column=1)
# Want to show quotes in the canvas
canvas.grid(row=1,column=1)

window.mainloop()