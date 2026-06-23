# Steps to follow debugging

1. Describe the Problem

- [task_1.py](./task_1.py)

```python
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")

my_function()

# Describe the problem
# What is thhe for loop doing?
# When is the function ment to print "You got it"?
# What are your assumptions about the value of i?
```

2. Reproduce the bug

- [task_2.py](./task_2.py)

```python
from random import randint
dice_images = ["1", "2", "3","4","5","6"]
dice_num = randint(1, 6)
print(dice_images[dice_num])

# This will ocassionally produce an error
```

3. Play Computer and Evaluate each line

- [task_3.py](./task_3.py)

```python
year = int(input("What's your yeam of birth?"))

if year > 1980 and year < 1994:
    print("You are a Millennial")
elif year > 1994:
    print("You are Gen Z.")

""" 
    Play Computer and go through the code line by line as if you are 
    executing code to figure out why 1994 does not work as expected.
    Then go aheadand fix the code.
"""
```

4. Fixing Errors and Watching for Red Underlines

- [task_4.py](./task_4.py)

```python
age = int(input("How old are you?"))
if age > 18:
print("You can drive at {age}.")

"""
    Fix any errors (red underline) that shows up in the editor before you 
    run your code. The warnings (yellow) are optional fixes, sometimes it
    will cause a problem down the line other times it is fine and the 
    editor just doesnt understand what you're trying to do.
"""
```

5. Using print statement

- [task_5.py](./task_5.py)

```python
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
```

6. Use a Debugger
- [task_6.py](./task_6.py)

> Platforms
- [Python Tutor](https://pythontutor.com)
- [Thonny Debugger Editor](https://thonny.org/)

```python
"""
    Most IDEs (Intelligent Development Environments) such as PyCharm will
    have built-in tools for debugging. This is normally known as the
    debugger. In many ways, they are like print statements on steroids.

    Debuggers allows us to peek into our code during execution and pause 
    on chosen lines to figure out what is the inner mechanism and where
    it's going wrong.

    There are a couple of things that are the same in most IDEs which you 
    should be familiar with:

    1. Breakpoint - You can set a breakpoint by clicking on a line in the 
    gutter of the code (where the line numbers are). This line will be 
    where the program pauses during debug run.

    2. Step Over - This button will go through the execution of your code
    line by line and allow you to view the intermediate values of your
    variables.

    3. Step Into - This will enter into any other modules that your code
    references. e.g. If you use a function from the random module it
    will show you the original code for that function so you can better
    understand its functionality and how it relates to your problems.

    4. Step Into My Code - This does the same thing as Step Into, but it
    limits the scope to your own project code and ignores library code
    such as random.
"""
import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

```