import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
movie_rank = []
movie_name = []
response = requests.get(url=URL)
movies100_web_page = response.text
soup = BeautifulSoup(movies100_web_page, "html.parser")
titles = soup.find_all(name="h3", class_="title")
"""
x = (titles.getText())
print(x)
y = x.replace(")", "")
print(y)
print(y.split())
z = y.replace(y.split()[0], "")
print(z)
"""
movie_titles = [title.getText() for title in titles]
movie_titles_sorted = movie_titles[::-1]

for title in movie_titles_sorted:
    new_title = title.replace(")", "")
    rank = new_title.split()[0]
    movie_rank.append(rank)
    name = new_title.replace(rank, "")
    movie_name.append(name)

print(movie_name)
print(movie_rank)
print(len(movie_name))
with open("movies.text", mode="w", encoding="utf-8") as file:
    for i in range(len(movie_name)):
        ranking = movie_rank[i]
        file.write(f"{movie_name[i]} - {ranking}\n")