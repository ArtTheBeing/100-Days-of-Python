from bs4 import BeautifulSoup
import requests
import csv
url = f'https://www.zillow.com/toronto-on/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A43.91272974955984%2C%22east%22%3A-79.112712625%2C%22south%22%3A43.50274043681314%2C%22west%22%3A-79.640056375%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%7D'
class Gather():
    def __init__(self, url):
        self.url = url
        
        self.parser()




    def parser(self):
        places = []
        response = requests.get(self.url, headers={'User-Agent': 'Chrome'})
        parse = BeautifulSoup(response.text, 'html.parser')
        #Data Finding
        price_elements = parse.find_all(attrs={"data-test": "property-card-price"})
        link_elements = parse.find_all('a', attrs={"data-test": "property-card-link"})
        address_elements = parse.find_all(attrs={"data-test": "property-card-addr"})
        #Data Cleaning
        prices = self.price_cleaner(price_elements)
        links = self.link_cleaner(link_elements)
        addresses = self.address_cleaner(address_elements)
        #Data Formatting
        for i in range(len(addresses)):
            places.append((prices[i], links[i], addresses[i]))
        self.write(places)

    def price_cleaner(self, price_elements):
        prices = []
        for element in price_elements:
            string = element.text
            string = string.split('$')
            string = string[1]
            if '+' in string:
                string = string.split('+')[0]
            else:
                string = string.split('/')[0]
            prices.append(string)

        return prices

    def link_cleaner(self, link_elements):
        base_url = "https://www.zillow.com"
        links = []
        visited_links = set()  # To track visited links and avoid duplicates
        for element in link_elements:
            href = element['href']
            if base_url not in href:
                    href = base_url + str(href)
            if href not in visited_links:
                links.append(href)
                visited_links.add(href)
        return links

    def address_cleaner(self, address_elements):
        addresses = []
        for element in address_elements:
            addresses.append(element.text)
        return addresses
    
    def write(self, tuples):
        with open('data.csv', 'w', newline= '') as file:
            writer = csv.writer(file)
            writer.writerows(tuples)
run = Gather(url)

