from tkinter import * # type: ignore

"""
TODO Create a layout where:
Label - column=0, row=0
Button - column=1, row=1
NewButton - column=2, row=0
Entry - column=3, row=3
"""

window = Tk()
window.title('Grid Challenge')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="First Label")
my_label.grid(column=0, row=0)

my_button = Button(text="Click Me!")
my_button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=3, row=3)

window.mainloop()