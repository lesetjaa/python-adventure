# Notes - Classes

## Class

- A blueprint for creating an eventual object

### How we create our own classes

```python
"""
We use PascalCase to name our classes (capitalize each first letter of
a word)
"""
class User:
    pass

user_1 = User()

```

- To create a class, we start with the `class` keyword and the name of our class
- Everything in the class will be indented after the semicolon
- In the last line we create an object from our class

### How to add attributes to our class

- This is the manual way of adding attributes, not recommended

```python
""" We can use the dot notation to add an attribute to our class """

user_1 = User()
user_1.id = "001 <- id attribute added
```

## Constructors

- A part of the blueprint that allows us to specify what should happen when
  our object is being constructed -> also knows as initializing

### How to create the constructor

```python
""" We use the init function """
class User:
    def __init__(self):
        pass
    pass
```

- This function is normally used to initialize the attributes
- It is called everytime we create a new object from the class

### How to create the attributes

```python
class Car:
    def __init__(self, seats):
        self.seats = seats

car_1 = Car(5) # same as v
# car_1.seats = 5
```

- You can add parameters to the function, and it will pass in when an
  an object is being constructed fro the class
- Once we recieve it we can use it to set the object's attributes
- If parameters are added to the class constructor, everythime an object
  is created, we have to put in the arguments

### To create default values

```python
class User:
    def __init__(self):
        self.followers = 0 # <- default to 0 with every user
        # There is no need to add the parameter
```

### Adding methods to the class

- Functions attached to a class are called methods
- Methods are the things that the object does

```python
class Car:
    def enter_race_mode(self):
        self.seats = 2
```

- There should be a self parameter in every method
- This means when the method is called, it know the object that called it
