# Notes - Snake Game Part 2

## Class Inheritence OOP

````python
class Animal:
    def __init__(self) -> None:
        self.num_of_eyes = 2

    def breathe(self):
        print("Inhale, Exhale!")
```

```python
from animal import Animal

class Fish(Animal) {
    def __init__(self):
        super().__init__()

    ç
        super().breathe()
        print("Doing this underwater")
}
````

### How to inherite from another class

```python
# Animal is the class the we want to inherite from, it is the super class
class Fish(Animal) {
    def __init__(self):
        super().__init__()
}
```

- This is to get the `methods` and `attributes` from Animal (parent) class

### How to add more to the function for specific child class

```python
def breathe():
        super().breathe() #<- Here
```

- We call the function from the parent class the continue to add the functionality from there

## Slicing

- This is used to get any section from a list or a tuple

### How to slice in python

```python
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_keys[2:5]) # gets [c, d, e]

print(piano_keys[2:]) # [c, d, e, f, g]

print(piano_keys[:5]) # [a, b, c, d, e]

print(piano_keys[2:5:2]) # [c, e]

print(piano_keys[::2]) # [a, c, e, g]

print(piano_keys[::-1]) # [g, f, e, d, c, b, a]

print(piano_tuple[2:5]) # ("mi", "fa", "so")
```
