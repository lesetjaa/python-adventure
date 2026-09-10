# Notes

## How to extend a widget with grid layout

- We use a `columnspan` to extend a widget into the next columns

```python
b = Label(bg="blue", width=40, height=5)
b.grid(row=2, column=0, columnspan=2)
```

## How to focus on a widget on app launch

- We use the `focus` method on that specific widget

**_Note:_**

- Only one widget gets focused so use it on only one widget

```python
website_entry.focus()
```

## How to add a starting value to an entry

- When we have an entry that we often use the same input in, we can prefill it on app launch
e.g. email entry, we use one email so often we can prefill it in the email/username entry

```py
# index: where would you like it to be placed
# string: what we place
email_entry.insert(index, string)

# e.g.
email_entry.insert(0, "hello@lesetja.dev")
```

## How to clear an entry

- After we make our operations, to clear an entry we use the delete method

```py
# start: start of the range
# end: end of range
email_entry.delete(start, end)

# e.g.
email_entry.insert(0, tk.END) # END- tkinter's end constants to get the last item
```
## Pop-ups