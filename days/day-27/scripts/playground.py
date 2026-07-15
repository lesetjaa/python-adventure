""" TODO
Modify the add function to take an unlimited number of arguments
Use a loop to sum all the arguments inside the function
Test it out by calling add() to calculate sum of some arguments.
"""

def add(*args):
    total = 0
    for number in args:
        total += number
    return total

print(add(1, 2, 3))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)

calculate(2, add=3, multiply=4)

# Creating a class
class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="BMW")
print(my_car.model)
