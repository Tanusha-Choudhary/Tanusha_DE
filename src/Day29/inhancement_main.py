from re import search
from tkinter import *
from tkinter import Image
from tkinter import messagebox
from PIL import Image, ImageTk
import pyperclip
import random
import json
# Password Generator
def search_button():
    website = website_entry.get()
    try:
        with open("Password.json","r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No data file found")
    else:
        try:
            if website in data:
                email = email_entry.get()
                password = password_entry.get()
                messagebox.showinfo(title="website",message=f"{website}\n password:{data[website]["password"]}")
            else:
                messagebox.showinfo(title="Nodata",message=f"No deatils found for {website}")
        except ValueError:
            messagebox.showinfo(title="Error",message=f"TBD")

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*','(', ')', '-', '_', '=', '+', '[',']', '{', '}', ';', ':', "'", '"',',', '.', '<', '>', '/', '?', '\\', '|','`', '~']
    nr_letters = random.randint(8,10)
    nr_symbols= random.randint(2,4)
    nr_numbers = random.randint(2,4)
    password_letters= [random.choice(letters) for _ in range(nr_letters)]
    password_symbols= [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers= [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    # password = ""
    # for i in password_list:
    #     password += i
    # print(f"your generated password {password}")
    password_entry.delete(0, END)
    password_entry.insert(0,password)
    # password_entry.delete(0, END)
    pyperclip.copy(password)

# Main code
def clicked():
    password = password_entry.get()
    email = email_entry.get()
    website = website_entry.get()
    new_data = {website: {"email": email,"password": password}}
    if len(password)==0 or len(website) ==0:
        messagebox.showerror("Oops", "Password must be between 8 and 16 characters")
    else:
        is_ok=messagebox.askokcancel(title="website",message=f"There are the details entered:\nEmail:{email}\nPassword:{password}\nWebsite:{website}")
        if is_ok:
            try:
                with open("Password1.json","r") as file:
                    # Reading the old data
                    data = json.load(file)
            except FileNotFoundError:
                with open("Password1.json","w") as file:
                    json.dump(new_data, file,indent=4)
            else:
                # Updating the data
                data.update(new_data)
                with open("Password.json","w") as file:
                    # Saving the data
                    json.dump(data,file,indent=4)
            finally:
                password_entry.delete(0, END)
                website_entry.delete(0, END)

# window
window = Tk()
window.config(padx=50, pady=50)
window.title("password manager")
# Image
image = Image.open("lock.png")
image = image.resize((100, 100))
img = ImageTk.PhotoImage(image)
# Canvas
canvas = Canvas(window, width=200, height=200, bg="white",highlightthickness=0)
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)
# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label=Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1,columnspan=2)
email_entry.insert(0,"xyz@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_button=Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3, column=2)
button_add =Button(text="Add",width=36,command=clicked)
button_add.grid(row=4, column=1,columnspan=2)
button_search =Button(text="Search",command=search_button,width=13)
button_search.grid(row=1, column=2)
window.mainloop()