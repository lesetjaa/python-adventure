from selenium import webdriver
from selenium.webdriver.common.by import By

# TODO - Get upcompung events from python.org; print them out in dictionary form
URL = "https://www.python.org/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(url=URL)
events = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')

events_cleaned = {}

for event in events:
    full_event = event.text.splitlines()
    event_dict = {"time": full_event[0], "name":full_event[1]}
    events_cleaned[len(events_cleaned)] = event_dict

print(events_cleaned)
driver.quit()