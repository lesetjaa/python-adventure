import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]

with open("movies.txt", mode="w") as file:
    for movie in titles[::-1]: # reverse list
        file.write(movie + "\n")
