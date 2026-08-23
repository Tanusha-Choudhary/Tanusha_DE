print(" Miles is equal to 32 km")
from tkinter import *
def calculate():
    print("Miles is equal to")
    miles = input_miles.get()
    miles = float(miles)
    print(miles)
    int_miles = miles * 1.60934
    text_label.config(text=int_miles)
window = Tk()
window.title("Miles to Km conveter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

# LABEL1
Miles_label = Label(text="Miles",font=("Times New Roman",14),fg="black",bg="white")
Miles_label.grid(row=0,column=3)
# LABEl2
is_equal_to_label = Label(text="is equal to",font=("Times New Roman",14),fg="black",bg="white")
is_equal_to_label.grid(row=1,column=1)
# LABEl3
text_label = Label(text="0")
text_label.grid(row=1,column=2)
# LABEL4
km_label = Label(text="Km",font=("Times New Roman",10),fg="black",bg="white")
km_label.grid(row=1,column=3)


# ENTRY1
input_miles = Entry(width=10)
input_miles.grid(row=0,column=2)

# BUTTON1
cal_button= Button(text="Calculate",command=calculate)
cal_button.grid(row=2,column=2)

window.mainloop()