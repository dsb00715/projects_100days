from bs4 import BeautifulSoup

with open("day45_beautifulsoup_movies\website.html", "r", encoding="utf8") as f:
    contents = f.read()

# soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.string)
# print(soup.prettify)
# print(soup.p)


# all_anchor = soup.findAll(name="a")
# print(all_anchor)

# for tag in all_anchor:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")

# class_is_heading = soup.find(class_="heading")

# h3_heading = soup.find_all("h3", class_="heading")


# name = soup.select_one(selector="#name")
# headings = soup.select(selector=".heading")
