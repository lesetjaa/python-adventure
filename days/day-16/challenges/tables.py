from prettytable import PrettyTable

table = PrettyTable()

""" Challenge 1 - Print a table """
table.add_column("Pokemon Name", [
    "Pikachu",
    "Squirtle",
    "Charmander"
])

table.add_column("Type", [
    "Electricity",
    "Water",
    "Fire"
])
print(table, end="\n")


""" Challenge 2 - Change the alignment attributes of the table """
table.align = "l"
print(table, end="\n")