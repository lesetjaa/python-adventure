from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://appbrewery.github.io/fake-newsletter-signup/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

name = driver.find_element(By.NAME, "fName")
name.send_keys("Lesetja")

name = driver.find_element(By.NAME, "lName")
name.send_keys("Malapane")

name = driver.find_element(By.NAME, "email")
name.send_keys("malapanelkd@gmail.com")

btn = driver.find_element(By.TAG_NAME, "button")
btn.click()
# btn.send_keys(Keys.ENTER)