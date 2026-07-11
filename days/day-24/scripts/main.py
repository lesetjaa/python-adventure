# file = open("my_file.txt")
# contents = file.read()
# print(contents)

# TODO - Move my_file to Desktop and fix the code so that it does not return an error

file = open("/Users/lesetja/Desktop/my_file.txt")
contents = file.read()
print(contents)

# TODO - Change it to use relative file path

file = open("../../Desktop/my_file.txt")
contents = file.read()
print(contents)
