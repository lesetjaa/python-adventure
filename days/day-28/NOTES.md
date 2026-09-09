# Notes

## Canvas Widget

- Allows us to lay on top something over another, in our case it allows us to place an image, and place the timer on top of the image

```python
from tkinter import *

canvas = Canvas(width=200, height=224) # about the same size as our image
tomato_img = PhotoImage(file="tomato.png") # image location
canvas.create_image(100, 112, image=tomato_img)
canvas.pack()
```

**_Notes_:**
- Canvas class allows us to place items on top of other times
- `image` tag in create_image requires a PhotoImage
- `PhotoImage` is a built-in class used to display graphic images in widgets like labels, buttons, canvases, and text fields
- `pack()` to place it on the window

## After (tkinter function)

- the `after` method allows us to call a function after a period of time

```python
window.after(1000, func, "Hello" )
```
**_Notes_:**
- `1000` -> time in millisec that the fuction to be called
- `func` -> function to be called
- `**args` -> agruments that will be passed into the function

## Dynamic Typing

- When a variable's data type can change during the execution of a program.

```python
x = 10        # int
x = "Hello"   # string
x = 3.14      # float
```