"""

# year = int(input("What's your yeam of birth?"))
year = 1994 # as a computer

# if year > 1980 and year < 1994:
# if True and False: # First condition True but second condition False
if False: # Which makes this statement False
    print("You are a Millennial") # No execution
# elif year > 1994: # 1994 is not greater than 1994
elif False:
    print("You are Gen Z.") # No execution

"""

# Solution

birth_year = int(input("What's your yeam of birth?"))

if birth_year > 1980 and birth_year < 1994: 
    print("You are a Millennial")
elif birth_year >= 1994: # include 1994 with ">="
    print("You are Gen Z.")
