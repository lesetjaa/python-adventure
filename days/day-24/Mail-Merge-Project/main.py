with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter = letter_file.read()

with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.read().split("\n") # .readlines() better

for name in names:
    with open(f"./Output/ReadyToSend/Letter_for_{name}.txt", mode="w") as new_letter:
        new_letter.write(letter.replace("[name]", name))
