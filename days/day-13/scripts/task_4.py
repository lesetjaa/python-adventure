# # age = int(input("How old are you?")) # input 'twelve'\
# age = 'twelve'
# if age > 18:
#     print("You can drive at {age}.") # indentation error (red lined) fixed also it should be an f string


# Solution

"""
    Wrap the code in a try block
"""

try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in an invalid number. Please try again with a numerical response such as 15.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at {age}.")