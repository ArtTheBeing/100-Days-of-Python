from bs4 import BeautifulSoup
url = 'https://news.ycombinator.com/'
import requests
response = requests.get('https://news.ycombinator.com/')

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_texts = []
article_links = []
articles = soup.find_all(class_ = 'titleline')
for article_tag in articles:
    article_links.append(article_tag.find('a')['href'])
    article_texts.append(article_tag.getText())


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name = 'span', class_ = 'score')]
print(article_texts)
print(article_links)
print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])
