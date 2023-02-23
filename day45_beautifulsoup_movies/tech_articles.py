import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")
article_text = []
article_link = []

articles = soup.find_all(name="span", class_="titleline")
for article_tag_span in articles:
    article_text.append(article_tag_span.a.get_text())
    if "item?id=" in article_tag_span.a.get("href"):
        article_link.append(
            "https://news.ycombinator.com/" + article_tag_span.a.get("href")
        )
    else:
        article_link.append(article_tag_span.a.get("href"))

article_scores = [
    int(score.get_text().split(" ")[0])
    for score in soup.find_all(name="span", class_="score")
]

largest_number = max(article_scores)
largest_index = article_scores.index(largest_number)

text = article_text[largest_index]
link = article_link[largest_index]

print(text)
print(link)
print(largest_number)
