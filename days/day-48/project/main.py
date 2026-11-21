from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://ozh.github.io/cookieclicker/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

time.sleep(3)  # wait for the page to load

try:
    eng_choice = driver.find_element(By.ID, "langSelect-EN")
    print("English Option Found, Clicking...")
except Exception as e:
    print("Option was not found...")
else:
    eng_choice.click()

time.sleep(1)

cookie = driver.find_element(By.ID, "bigCookie")


def buy_item():
    items = driver.find_elements(By.CLASS_NAME, "product")
    prices = [price.text.replace(",", "") for price in driver.find_elements(By.CLASS_NAME, "price")]
    print(prices)
    cookie_count = driver.find_element(By.ID, "cookies")
    cookies = cookie_count.text.split()[0]

    for item in items:
        if float(cookies) > float(prices[items.index(item)]):
            continue
        else:
            items[items.index(item) - 1].click()
            break


try:
    timeout = time.time() + 5   # 5 minutes from now
    while True:
        cookie.click()
        if time.time() > timeout:
            buy_item()
            time.sleep(1)
            timeout = time.time() + 5
except KeyboardInterrupt:
    driver.quit()
