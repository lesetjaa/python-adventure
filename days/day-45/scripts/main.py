from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name) # title
# print(soup.title.string) # Angela's Personal Site

# print(soup.prettify()) 

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     tag.get_text()
#     tag.get("href")

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.name)
# print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
assert company_url is not None
print(company_url.get("href"))

# OR
name = soup.select_one(selector="#name")
print(name)

# OR
head = soup.select_one(selector=".heading")
print(head)