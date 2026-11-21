# Notes

## Selenium Webdriver

- Selenium Webdriver helps us create these chains of continuous actions like `clicking` a button or `typing` in a search box on the web

### Using Selenium Webdriver

```python
from selenuim import webdriver

driver = webdriver.Chrome()
```

- The `webdriver` module will be the one responsible for our automated tasks

#### Opening a webpage

```python
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
```

- Before we access a webpage, we need to setup our browser options to keep open after the program is done
- `webdriver.ChromeOptions()` we get ahold of the browser option
- `add_experimental_option("detach", True)` add an option to keep webpage open after the program finishes
- Then we pass the configuration to our webdriver

```python
driver.close()
driver.quit()
```

- We can also close the current webpage manually with `driver.close()`
- with `driver.close()` we can close the entire browser

### How to find and locate html elements

```python
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
element = driver.find_element(By.CLASS_NAME, "information")
```

- Selenium uses a `By` class, it has helpers such as `By.CLASS_NAME` to help locate elements by their class name

**_Note:_** To get the text from the element we use `.text` on the element

#### Useful Selenium locator

```python
driver.find_element(By.NAME, "q")
print(search_bar.tag_name) # input
print(search_bar.get_attribute("placeholder")) # Search
```

- In [python.org](https://python.org), the search bar has a name attribute with the value `"q"`

```python
button = driver.find_element(By.ID, value="submit")
print(button.size) # {"height": 40, "width": 20}
```

- Once we get these elements we can get various properties

```python
driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
```

- We can also find elements by css selector

#### If all else fails,XPath

```python
tricky_elemment = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
```

- To use the XPath, we need to inspect the element we want the copy its XPath (in chrome developer tools)
- Then we use the find by XPath to get the element

**_Note:_** All the find methods have counter methods which find all the elements and returns them in a list


### How To Interacte with elements

#### Clicking links

```python
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
article_count.click()
```

- We need to get ahold of the element and call the `click()` method

```python
all_portals = driver.find_element(By.LINK_TEXT, "Content portal")
all_portals.click()
```

- We can also create an object by tapping into find_element by link text
- `Content portal` - this is the text we see on the page4

#### Typing in input elements

```python
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
```
- Firstly, Get a hold of the input element
- `send_keys("")` - use the send keys method to type in the input box, in this case we typed Python in the search bar

#### Entering keyboard keys

```python
from selenium.webdriver.common.keys import keys

# search.send_keys(Keys.ENTER)
search.send_keys("Python", Keys.ENTER)
```

- After entering our data on the search bar with selenium, we can also trigger a keyboard action `Enter/ Return` key
- We have to import the `Keys` from selenium packages
- We trigger the enter keys in the `send_keys()` method