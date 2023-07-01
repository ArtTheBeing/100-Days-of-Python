import requests
from bs4 import BeautifulSoup
response = requests.get(url='https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')

soup = BeautifulSoup(response.text, 'html.parser')
titles = [title.getText() for title in soup.findAll(name = 'h3', class_ = 'title')]
titles.reverse()

with open (file= "Day 45/bs4-start/top100movies.txt", mode= 'w', encoding='utf-8') as file:
    for title in titles:
        file.write(title + '\n')

