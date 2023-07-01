import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        self.urlbase = 'https://www.nike.com/w/mens-clothing-6ymx6znik1'
        self.clothes = {}
        self.urls = {}
        self.prices = {}

    def objective(self):
         print("Clothes Only")

    def scrape(self):
        response = requests.get(self.urlbase).text
        soup = BeautifulSoup(response, 'html.parser')
        items = soup.select(selector = 'div figure a.product-card__link-overlay')
        prices = soup.select(selector= 'div.product-price__wrapper')

        #tokenization to keep track
        for i, item in enumerate(items):
                self.urls[i] = item.get('href')
                self.clothes[i] = (item.getText().strip())
        
        for i, item in enumerate(prices):
             if item.get('aria-label') == None:
                  print('no disc')
             else:
                self.prices[i] = (item.get('aria-label'))
s = Scraper()
s.scrape()

print(s.urls)
print(s.clothes)
print(s.prices)