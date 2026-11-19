from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/") # html file content
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# first_story = soup.select_one(selector=".storylink")

articles = soup.find_all(name="a", class_="storylink")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.get_text()
    link = article_tag.get("href")

    article_texts.append(text)
    article_links.append(link)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

# TODO - print the title with the highest number of upvotes

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])