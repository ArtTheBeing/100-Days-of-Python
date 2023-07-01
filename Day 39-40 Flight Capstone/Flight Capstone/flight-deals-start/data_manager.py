import requests
from pprint import pprint

class DataManager:
    def __init__(self):
        self.url = 'https://api.sheety.co/344c69e7d5b351a6b79f3543079fe62d/copyOfFlightDeals/prices'
    
    def get_info(self):
        response = requests.get(url =self.url)
        return (response.json()['prices'])
    
    def update(self, json):
        for city in json:
            response = requests.put(url=f"{self.url}/{city['id']}", json= {'price': city})
            print(response.text)

data = DataManager()
data.get_info()
