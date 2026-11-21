from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.python.org/")

# driver.get(url="https://www.amazon.co.za/Sony-WH-1000XM6-Headphones-Microphones-Studio-Quality/dp/B0F3PQHWTZ/ref=cs_sr_dp_2?crid=31WW137SBCMHH&dib=eyJ2IjoiMSJ9.G6fW22-sksvlrv2CemSOkdCDvOilr-FWrpPy48cYA1xypln1SrmA0FP-A3xy0eKpW04609_Gfle0HmZ_0UYkKYvGFf5X4VAyx1ky4fk1PAPc2ci1SAXGsTvvJQO6dYa0jQVURqf4QHpGv6xgEBnuWyacK29gi2IojwV6dHhxtMFG0fOn5iWCq-tjnxoDFHcfhM8ei7VFvXdqk-1IOfXZsQwymNJhBOJGDu57UEnBXm3aD1uSemwkeuRb1n8uqna1mnyOi7bCBt3wNLZOUjSQsWU5tEapL1kFkkB3OYzpLXk.Fv__I9rxm4rZQkdrGg2SzZQaTp6atp_BZa3Mq2KI-rw&dib_tag=se&keywords=Sony%2BWH-1000XM6&qid=1795173744&sprefix=sony%2Bwh-1000xm6%2Caps%2C569&sr=8-3&th=1")
# price_rands = driver.find_element(By.CLASS_NAME, value="a-price-whole") # element
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction") # element

# print(f"This is the price: {price_rands.text}.{price_cents.text}")

search_bar = driver.find_element(By.NAME, "q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))


button = driver.find_element(By.ID, value="submit")
print(button.size)

link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(link.text)


bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# driver.close()
driver.quit()