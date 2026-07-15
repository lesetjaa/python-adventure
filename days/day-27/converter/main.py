from tkinter import Button, Label, Tk, Entry

"""
Create the Miles to Km converter with Tkinter
"""


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(column=1, row=0)



def convert():
    """Converts the input value"""
    number = 1.60934 * int(input.get())
    converted_value.config(text=str(number))


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

converted_value = Label(text="0")
converted_value.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calc_btn = Button(text="Calculate", command=convert)
calc_btn.grid(column=1, row=2)
calc_btn.config(padx=10, pady=10)


window.mainloop()
