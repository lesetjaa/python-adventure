# Notes

## Getting started with Beautiful Soup

- Beautiful Soup is a python library for pulling data in a HTML and XML file.

```python
# Basic scraping with our local file
from bs4 import beautifulsoup

with open("html-file.html") as file:
    contents = file.read()
```

- we import beautifulsoup from the bs4 module
- then we open our local html file, read it and save it as contents

```python
soup = BeautifulSoup(contents, "html.parser")
```

- we create a new beautiful soup object and pass in:
  - `markup` text (contents)
  - parser ("html.parser") this helps beautiful soup what these `contents` are structured in (html/ xml)

**For xml:**

```python
import lxml

soup = BeautifulSoup(contents, "lxml")
```

### To get information from our html file

```python
soup.title()
```

```html
<!-- Output -->
<title>Angela's Personal Site</title>
```

- we use the soup object to tap into our html file and get specific content we want.

```python
print(soup.a)
```

- This gets a hold of the first a tag of the page

**_Note:_** We use the html tags on our python object to get the data from the html file.

### How to get all the specific tag

```python
soup.find_all(name="a")
```

- Here we are searching by tag `name`
- We are looking for all the tags where the tag name is `a`

#### Go deeper and get data fro tag

```python
tag.get_text()
```

- We can use this to get the text from the anchor tag.

**Trick:** use `find_all()` to get the all `anchor tags`, loop through and use `.get_text()` to get the data from the tag

#### To get the attribute value

```python
tag.get("href")
```

- Here we are getting the `href link` from the tag

**We can also use this:**

```python
soup.find_all(name="h1", id="name")
# soup.find_all(name="h1", class_="name")
```

- Here we are looking for all the `h1 element` with the id `"name"`

### How to narrow down to a specfic value

- For example: if a href is buried under multiple tags, we can use css selectors

```python
soup.select_one(selector="p a")
```

### Web scraping a live website

```python
from bs4 import BeautifulSoup
import requests

data = requests.get("website")
html_content = data.text
soup = BeautifulSoup(html_content, "html.parser")
```

- We start by downloading the html file using requests
- get the html contents using the `<object>`.text
- Then pass it into beautiful soup to begin web scraping

#### To check what we are allowed to web scrap from a website, go to `/robots.txt` endpoint of the website

- example:
  - [Netflix Robots endpoint](https://www.netflix.com/robots.txt)
