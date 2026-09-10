from tkinter import *  # type: ignore
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def confirm(website, username, password):
    return messagebox.askokcancel(title=website, message=f"Username: {username}\nPassword: {password}\nAre you sure you want to save these")


def is_valid(website, username, password):

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Missing Values", message="Some values seem to be empty, fill in all the values")
        return False
    return True


def save():
    """Saves the data into data.txt file"""

    data = get_data()
    website = data["website"]
    username = data["username"]
    password = data["password"]

    if is_valid(website, username, password):
        if confirm(website, username, password):
            with open(file="data.txt", mode="a") as file:
                file.write(
                    f"{website}  |  {username}  |  {password}\n")

            clear_entries()


def get_data():
    """Fetches values from entries, returns them formatted"""
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    return {
        "website": website,
        "username": username,
        "password": password
    }


def clear_entries():
    """Clears the entries"""
    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)

image_png = PhotoImage(file="logo.png")
# positions (100, 100) from canvas sizes (200, 200)
canvas.create_image(100, 100, image=image_png)
canvas.grid(column=1, row=0)

# website widgets
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# username widgets
username_label = Label(text="Email/Username:",)
username_label.grid(column=0, row=2)

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "hello@lesetja.dev")

# password widgets
password_label = Label(text="Password:", )
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3)

# Add btn
add_password_btn = Button(text="Add", width=36, command=save)
add_password_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()
