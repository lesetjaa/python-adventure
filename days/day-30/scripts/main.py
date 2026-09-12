# FileNotFound
# with open("file1.txt") as file:
#     file.read()

# KeyError
# a_dict = {"key": "Value"}
# value = a_dict["non_existent_key"]

# IndexError
# fruit_list = [""]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)


# try file
try:
    file = open("a_file.txt")  # FileNotFoundError
    a_dict = {"key": "value"}
    print(a_dict["key"])

except FileNotFoundError:
    file = open("a_file.txt", "w")  # create the file if it does not exist
    file.write("Something")

except KeyError as error_message:
    print(f"The key {error_message} does not exist")

else:
    content = file.read()
    print(content)

finally:
    file.close()  # type: ignore
    print("File was closed")

# Calculating bmi
height = float(input("Height"))
weight = float(input("weight"))

if height > 3:
    raise ValueError("Your height is over 3 meters")

bmi = weight / height ** 2
