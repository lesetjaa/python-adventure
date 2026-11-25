# Notes

```py
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
```

- To give selenium its own user profile, so that the next time we log in it remembers our data instead of creating an new one
- `user_data_dir` - we create our working directory path
- `f"--user-data-dir={user_data_dir}"` - we point to where out chrome_profile is
- `chrome_options.add_argument()` - then finnaly add it to the webdriver through chrome options

**_Pro tip 1:_** Use WebDriverWait instead of time.sleep(). [Waits Docs](https://www.selenium.dev/documentation/webdriver/waits/)
**_Pro tip 2:_** Use presence_of_element_located to verify that an element is present on the page.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

wait = WebDriverWait(driver, timeout=2)

wait.until(EC.title_is("Web form - target page"))
message = wait.until(EC.presence_of_element_located((By.ID, "message")))

wait.until(EC.visibility_of(message))
wait.until(EC.text_to_be_present_in_element((By.ID, "message"), "Received!"))
```

- Instead of using `time.sleep()`, we can use a tool be selenium called `WebDriverWait`
- This gives us the ability to wait for a particular element we mention for a the time we set
- Once that element appears, the script can continue instead of sleeping for a set time which could be longer
