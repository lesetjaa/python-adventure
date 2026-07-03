# Notes - More on Turtle Graphics

## Event Listeners

A programming procedure that waits for a specific activity or event to occur such as a user clicking a button or pressing a key using a keyboard

### Using Event Listeners with Turtle module

- We get a hold of the creen object from turtle module and we tell it to start listening

```python
from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()

my_screen.listen()
```

> Now Once it starts listening, we have to bind a function that will be triggered when a particular key is pressed

- To bind a key to an event, we have to use an event listener
- We use the `onkey` function which expects a `function` and a `key`

```python

def move_forward():
    tim.forward(10)


my_screen.onkey(move_forward, "w")
```

- When thw 'w' key is pressed, the turtle moves forward.

### Higher Order Functions

- Passing a function into another function
- We only pass the function name, not the function with parenthisis
- This is called Higher Order Function, a function that can work with other functions

```python

""" function_b is a higher order function """
def function_a(something):
    # do something with `something`

# def function_b(function_a()) X
def function_b(function_a): /
    # Do this
```

- It is recomended to use key word arguments instead of positional arguments

```python

# my_screen.onkey(move_forward, "w")

""" Like this: """
my_screen.onkey(fun=move_forward, key="w")

```

## Object State and Instances

- When creating multiple objects from the same class, they are considered instances of that class
- These objects can have different attributes at the same time (one might be green, another might be red) this is know as their states
