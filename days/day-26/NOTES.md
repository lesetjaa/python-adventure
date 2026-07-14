# Notes

## List Comprehension

a case where you create a new list from a previous list

**Example**

```python

# Create a new list of these numbers added by 1
numbers = [1, 2, 3]
new_numbers = []
for number in numbers:
    new_number = number + 1
    new_numbers.append(number)

```

### Using List Comprehension

- We can take the last 4 lines of code from above and create a new list in just one line

```python

numbers = [1, 2, 3]

"""keyword pattern"""
# new_list = [new_item for item in list]

"""practical use"""
new_numbers = [number + 1 for number in numbers]
```

**_Note_**

- You can also do it for letters

## Conditional List Comprehension

It allows us to only add the new item if the test passes

```python

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

"""We want to create a new list of short names only"""

"""keyword pattern"""
# new_list = [new_item for item in list if test]
"""practical use"""
short_names = [name for name in names if len(name) < 5]
```

## Dictionary Comprehension

Similar to List Comprehension but for dictionaries

```python

""" Creating a dictionary from a list"""
new_dict = {new_key: new_value for item in list}

""" Creating a dictionary from values of another dictionary"""
new_dict = {new_key: new_value for (key, value) in dict.items()}

""" Also a test can be added """
new_dict = {new_key: new_value for (key, value) in dict.items() if test}

```

## Iterating over Pandas DataFrame

We use the panda's iterrrows method to loop through

```python
# Create DataFrame
student_dataframe = pandas.DataFrame(student_dict)

```

```python
# # Loop through DataFrame
for (key, value) in student_dict.items():
    print(value) # This is not particularly good (looping for values)

```

```sh
# output

0    Angela
1     James
2      Lily
Name: student, dtype: str
0    56
1    76
2    98
Name: score, dtype: int64
```

```python
""" Pandas has a inbuilt loop called iterrows """
# Loop through rows of a data frame

for (index, row) in student_dataframe.iterrows():
    print(row.score)

```

```sh
# output

student    Angela
score          56
Name: 0, dtype: object
student    James
score         76
Name: 1, dtype: object
student    Lily
score        98
Name: 2, dtype: object
```
