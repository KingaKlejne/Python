from tkinter import *
from tkinter import messagebox
from random import choice, randint, sample
import pyperclip
import json


def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters = [choice(letters) for _ in range(randint(8, 10))]
    numbers = [choice(numbers) for _ in range(randint(2, 4))]
    symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password = [*letters, *numbers, *symbols]
    password = sample(password, len(password))
    password = "".join(password)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if password == "" or website == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")

    else:
        try:
            with open("data.json", "r") as passwords_file:
                data = json.load(passwords_file)
        except FileNotFoundError:
            with open("data.json", "w") as passwords_file:
                json.dump(new_data, passwords_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as passwords_file:
                json.dump(data, passwords_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = website_entry.get().title()
    try:
        with open("data.json", "r") as passwords_file:
            data = json.load(passwords_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email_address = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email_address}\nPassword: {password}")
        else:
            messagebox.showwarning(title="Error", message="No details for the website exists.")


# UI Setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Buttons
button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(column=2, row=3)
button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2, sticky="EW")
button_search = Button(text="Search", command=find_password)
button_search.grid(column=2, row=1, sticky="EW")

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "abcdefgh@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

window.mainloop()
