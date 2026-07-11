# Notes - Working with Files

## How to Open, Read and Write to Files

### Reading a file

```python
file = open("../resources/my_file.txt")
contents = file.read()
print(contents)
file.close()
```

- the contents of the file will be printed out

**Note**

- When we open a file, it takes up some of the resources of the computer
- It will eventually close itself some other time but we do not know when and if it will be closed
- Therefore we have to manually close it to save up some resources

**Alternatively**

- We can use the `with` keyword
- This automatically manages the file closing so we dont have to remember to do so at the end of the code
- `as` keyword is an alias for the file

```python
with open("my_file") as file:
    contents = file.read()
    print(contents)
```

### Write to a file

```python
with open("my_file.txt", mode="w") as file:
    file.write("New Text")
```

- We use `mode="w"`to write to the file (this wipes the contents)

**More options**

- We can use `mode="a"`to add (append) to the file

**Note**

- opening a file non existing file with write mode will create a new file

## File paths

- Navigating through folders to get to files
- `"/"` is the start of the folder system for computers, it is called root
- This is the path for the current folder this file is in, (<name> -> name of pc):
- `/Users/<name>/Github/python-adventure/days/day-24`

### Absolute file path

- The absolute file path always start relative to the root
- this means that the file path always stary with `/`

### Relative file path

- The relative file path always start relative to the `working directory`
- meaning it starts from the folder we are working with
- To get to this file `NOTES.md` using relative file path, it is `./NOTES.md`
- `./` - this means look at the current foler

**To Go Back**

- use `../` to go back one folder and more `..` to go back further 
