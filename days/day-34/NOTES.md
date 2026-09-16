# Notes

## HTML entities

- These are characters that help HTML distinguish HTML code from other charaters

```html
<!-- 
The symbol '<' is norally used to start a div or p like this: '<div>'
if we want the less than sybol we use ' &lt; '
-->
3 &lt; 5
<!-- In a page view it will look like this "3 < 5" -->
```

## How to unescape HTML entites

- We can use the html module to access the unescape method and format out string to be a normal python string

```python
import html

unescaped_text = html.unescape(escaped_text)
```

## Type Hinting/ Type annotation

- A type hint is a way of indicating the expected data type of a variable, function parameter, or return value in Python.

```python
age: int

# can later be set/ declared
age = 12
```

## Type Hinting in functions

- In case we have a file with many lines of code and many functions
- We can use type hinting on functions to remind ourselves on what the function expects and what it returns

```python
# type hints in parameters

""" 'parameter: data type' """
def age_checker(age: int)

# type hinting function returns

""" '-> return type' """
def age_checker(age: int) -> bool:
    return bool
```
