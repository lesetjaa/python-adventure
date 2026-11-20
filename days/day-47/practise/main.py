# Static Website

import requests
from bs4 import BeautifulSoup


URL = "https://appbrewery.github.io/instant_pot/"
response = requests.get(URL)
response.raise_for_status()

html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

price_element = soup.find(name="span", class_="a-offscreen")
assert price_element is not None
price = float(price_element.get_text().split("$")[1])

print(price)

