from tkinter import *

def calculate():
    miles = float(input1.get())
    km = miles * 1.60934
    label4.config(text=f"{km:.2f}")

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

# Entry
input1 = Entry(width=10)
input1.grid(row=0, column=2)

# Labels
label1 = Label(text="Miles")
label1.grid(row=0, column=3)

label2 = Label(text="is equal to")
label2.grid(row=1, column=1)

label4 = Label(text="0")
label4.grid(row=1, column=2)

label3 = Label(text="Km")
label3.grid(row=1, column=3)

# Button
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=2)

window.mainloop()