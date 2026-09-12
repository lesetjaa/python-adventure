# Notes

## Catching Exceptions

- This helps us avoid errors and crashing of our program/code

```python
try:
    "Something that might cause an exception"

except:
    "Do this if there was an exception"

else:
    "Do this if there was no exception"
    "Only works when the except block was never executed"

finally:
    "Do this no matter what happend (exception or not)"
```

**_Note:_**

- Do not use a bare except block
- Meaning that we should specify what error we are trying the excpet

```python

# The following code will run successfully because both FileNotFoundError and KeyError will be caught
# the program will continue to run without throwing an Error
try:
    file  = open("some_file.txt") #FileNotFoundError
    test_dict = {"key": "value"}
    print(test_dict["non_existing_key"]) #KeyError
except:
    file.open("some_file.txt", "w")
    file.write("Something")

# we should catch a specific thing, the except should have what error we should catch

-> except FileNotFoundError:
-> except KeyError:

# Also we can have multiple except lines

```

## Getting hold of the error message

```python

# use an alias to get the message
except KeyError as error_message:
```

## Rasing Exceptions

- Use keyword `raise` to raise an error (from the known errors)

```python

raise KeyError
raise TypeError("This error is fictional")

```

## JSON files

- `JSON`-> JavaScript Object Notation
- This is used to transport data across the internet

```Json
{
    "Netflix": {
        "email": "angela@gmail.com",
        "password": "Yr)4h+nnoXg3#"
    },
    "Amazon": {
        "email": "angela@gmail.com",
        "password": "Yr)4h+nnoXg3#"
    }
}
```

## Working with JSON files (writing in JSON file)

| we use the json module (in-built)

- `file` opened json file we want to write/work on
- `dict` dictionary to be added
- `int` number of indentation for readability

- Here we are `serialize`, convert python object to JSON

```python

import json
with open("data.json", "w") as data_file:
    json.dump(<dict>, <file>=data_file, indent=<int>) # do not use the .write method
```

## Working with JSON files (reading a JSON file)

| we use the .load method from the json module

- Here we are `deserialize`, convert JSON back to python object

```python

import json
with open("data.json", "r") as data_file:
    json.load(data_file) # converts to dict
```

## Working with JSON files (update a JSON file)

| we use the .update method from the json module

````python

import json
with open("data.json", "r") as data_file:
    # read old data
    data = json.load(data_file)
    #Update the old data with new data
    data.update(new_data) # updates the data

with open("data.json", "w") as data_file:
    #Saving updated data
    json.dump(data, data_file, indent=4)

````
