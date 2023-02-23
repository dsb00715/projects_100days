import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")
movie_list = []

movies_div = soup.find_all(name="div", class_="article-title-description__text")

for movie in movies_div:
    movie_list.append(movie.h3.get_text())

sorted_list = movie_list[::-1]

with open("day45_beautifulsoup_movies\movies.txt", "a", encoding="utf-8") as f:
    try:
        for movie in sorted_list:
            f.write(movie)
            f.write("\n")
        print("done!Check out movies.txt")
    except:
        print("Couldn't save data! Please recheck.")
