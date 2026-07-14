import random
import pandas

# numbers = [1, 2, 3]

# # TODO - create a new list from numbers, where you add one to each value

# # new_numbers = [new_item for item in list]
# new_numbers = [number + 1 for number in numbers]


# name = "Angela"
# new_list = [letter for letter in name]

# # TODO - predict what new_list will contain

# # ["A", "n", "g", "e", "l", "a"]


# # TODO -  take the range between 1 - 5, double each number and put them in a new list

# doubled_range = [number * 2 for number in range(1, 5)]

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# # TODO - take names with the length of 5 or more and turn then into uppercase

# long_names = [name.upper() for name in names if len(name) > 5]

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# students_scores = {student: random.randint(1, 100) for student in names}
# passes_students = {student: score for (student, score) in students_scores.items() if score >= 60}

# print(passes_students)


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Loop through dictionaries
for (key, value) in student_dict.items():
    print(value)


# Create DataFrame
student_dataframe = pandas.DataFrame(student_dict)

# Loop through DataFrame
for (key, value) in student_dataframe.items():
    print(value) # This is not particularly good (looping for values)

"""Pandas has a inbuilt loop called iterrows"""
# Loop through rows of a data frame

for (index, row) in student_dataframe.iterrows():
    # print(row)
    if row.student == "Angela":
        print(row.score)