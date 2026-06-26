# Notes - OOP

## Object-Oriented Programming (OOP)

OOP helps structure code by combining data and behavior into reusable units called classes. This makes it easier to model real-world problems, keep code organized, and reduce duplication.

### Classes

- A class is a blueprint or template for creating objects.
- It defines attributes (data) and methods (functions) that belong to the object.
- Use `class ClassName:` to declare a class in Python.

### Objects

- An object is an instance of a class.
- Each object has its own state stored in attributes.
- You create an object by calling the class like a function.

## Creating objects

### Example: instantiating a class

```python
from turtle import Turtle

timmy = Turtle()
```

In this example:
- `Turtle` is the class.
- `timmy` is an object or instance of the `Turtle` class.

## Attributes and methods

- Attributes store object data. Example: `timmy.speed`
- Methods define behavior. Example: `my_screen.exitonclick()`

### Example with `turtle`

```python
from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()

current_speed = timmy.speed
my_screen.exitonclick()
```


