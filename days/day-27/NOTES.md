# Notes

## Using Tkinter

- This main loop holds on to the window and keeps on listening to see if there's anything else that the user is going to do to interact with that window so that it can respond when that happens

```python
import tkinter # preinstalled with python


window = tkinter.Tk()
window.mainloop()
```

**_Note_:**
To keep the window on the screen we have to have a while loop that keeps on running

### Working with Tkinter

- When we want to display components on the window with tkinter, we have to first create the component
- Then we have to specify how that component is going to be laid out on the screen before it shows up

```python
my_label = tkinter.Label()
my_label.pack() # Place the label
```

## Setting Default Values for Optional Arguments inside a Function Header

### Arguments with Default values

- Here we are setting up a function that already has values setup for its arguments
- When calling the function, you do not need to provide values for parameters that already have the default arguments. The function will automatically use those default values.
- This is only if you want to use the default avlues that were declared with the function.

```python
def my_function(a=1, b=2, c=3):
    # Do this with a
    # Then do this with b
    # Finally do this with c

my_function()
```

**_Note_:**
We can selectively modify any value we want, the rest will still take up the default values

```python
my_function(b=5)
```

**_Note 2_:**
When we do not give default values for the function, those values will be required when we call the function

```python

# word will be required when we call the function
second_func(word, font="Arial", size=8)

#error
second_func()

# Correct - word was provided, the rest take their default values
second_func("Hello World")
```

## Functions that can take any number of arguments

```python
def add(*args): # arguments
    for n in args:
        print(n)
```

- We use `*args` (tuple) to setup the function for an unlimited number of arguments
- We are not bound to using `*args`, as long as we have an asterisk in front of the word it will be taken as unlimited arguments e.g `*arguments`, `*values` -> these are the same as `*args`

### We can now pass in any number of values

```python
add(1, 4, 2, 4, 5, 6)
```

## Many keyword arguments

```python
def calculate(**kwargs): # key word arguments

```

- We use `**kwargs` (dict) to setup the functions for an unlimited number of key word arguments
- Same as `*args` we are not bound to using this word

## Creating a class with key word arguments

- Use `.get()` so that when the argument is not give a value, it does not return an error

```python
class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="BMW")
print(my_car.make)
```

## Tkinter Layout Managers

```python
from tkinter import *
component = Button()
```

### `.pack()` Method

This method places the components next to each other. Default -> Starts from to to bottom

```python
component.pack()
```

### `.place(x,y)` Method

This method is used for precise placement. We provide the x and y value

```python
component.place(x=0, y=0) # Top Left Corner
```

### `.grid()` Method

This method divides the window into a grid. It is relative to other components

```python
"""Top Left Corner if there are no other components otherwise it will go on specifed position"""
component.grid(column=1, row=1)
```

### Adding Padding

```python
window.config(padx=20, pady=200)
```