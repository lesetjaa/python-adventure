from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://en.wikipedia.org/wiki/Main_Page"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)
# TODO - Get the number of articles shown on the page and print it out

article_count = driver.find_element(By.ID, "mwDw")
print(article_count.text)