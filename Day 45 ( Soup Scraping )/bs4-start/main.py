from bs4 import BeautifulSoup
# some websites use lxml
import lxml

with open("website.html", encoding='utf-8') as file:
    content = file.read()

# lxml if html parser does not wor
soup = BeautifulSoup(content, "html.parser")
# print(soup.title)

all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
# print(tag.getText())
# print(tag.get("href"))
# print(all_anchor_tags)

heading = soup.find(name="h1", id="name")
section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.getText())
# CSS selector . # sign for id selection ( sample 2 )  or normal css for selector or element type ( sample 3 )
specific_select = soup.select_one(selector="p a")  # CSS selection
specific_select2 = soup.select_one(selector="#name")  # id selection
specific_select3 = soup.select_one(selector=".heading")  # element selection class
multi_select = soup.select(selector=".heading")  # ALL element selection , Return a list
print(multi_select)
