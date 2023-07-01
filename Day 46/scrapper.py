import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        self.urlbase = 'https://www.billboard.com/charts/hot-100/'
        self.when_top100()
        self.songs = []

    def when_top100(self):
        year = input("Give me a year: ")
        month = input("Give me a month: ")
        if len(month) == 1:
            month = '0' + month
        day = input("Give me a day: ")
        if len(day) == 1:
            day = '0' + day
        self.urlbase = f"{self.urlbase}/{year}-{month}-{day}"

    def scrape(self):
        response = requests.get(self.urlbase).text
        soup = BeautifulSoup(response, 'html.parser')
        songs = soup.select(selector = 'li ul li h3')
        for song in songs:
            self.songs.append(song.getText().strip())
    