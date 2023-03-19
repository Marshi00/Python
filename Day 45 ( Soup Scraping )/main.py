from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
"""
article_tag = soup.find(name="a", class_="titlelink")
article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvote = soup.find(name="span", class_="score").getText()
print(article_text, article_link, article_upvote)
"""
article_title = []
article_links = []
articles = soup.find_all(name="a", class_="titlelink")
for article_tag in articles:
    text = article_tag.getText()
    article_title.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(article_title)
# print(article_links)
# print(article_upvote)
largest_number = max(article_upvote)
largest_number_index = article_upvote.index(largest_number)
print(article_title[largest_number_index])
print(article_links[largest_number_index])