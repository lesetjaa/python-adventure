# import tkinter
from tkinter import *  # type: ignore

# Setting Up the Window

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

# Putting Labels
my_label = Label(text="I am a Label", font=("Arial", 16, "italic"))
my_label.pack()

# Ways of changing/configure components that we made
my_label["text"] = "New Text"
my_label.config(text="New Text!")

# TODO 1. Show 'Button Got Clicked' on my_label when the button gets clicked


def button_clicked():
    """event listener for the button"""
    print("Button Clicked")
    my_label.config(text='Button Got Clicked')

# TODO 2. When the button is clicked, it should change the label into the value you added into the input


def change_label():
    """Changes the label into the value from the input"""
    my_label.config(text=input.get())


# Button
# button = Button(text="Click Me!", command=button_clicked)
button = Button(text="Click Me!", command=change_label)
button.pack()

# Entry component
input = Entry(width=10)
input.pack()

# To get value from the input use `.get()` method
# data = input.get()


window.mainloop()
