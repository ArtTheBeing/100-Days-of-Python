import requests
import datetime as dt
from flight_data import FlightData
from pprint import pprint

class FlightSearch:
    def __init__(self):
        self.kiwi_api = ''
        self.kiwi_url = 'https://tequila-api.kiwi.com'
        self.headers = {"apikey" : self.kiwi_api}
        self.search_url = 'https://api.tequila.kiwi.com/v2/search'
    
    #Loop through google doc for city name and then plug that in here
    def destination_code(self, city_name):
        location_endpoint = f"{self.kiwi_url}/locations/query"
        
        query = {"term" : city_name}
        response = requests.get(url=location_endpoint, headers= self.headers, params= query)
        results = response.json()['locations'][0]['code']
        return results
        
    def flight_search(self, origin_city, destination_code, max_price):
        query = {
            'fly_from' : origin_city,
            'fly_to' : destination_code,
            'date_from' : dt.date.today().strftime(("%d/%m/%Y")),
            'date_to' : (dt.date.today() + dt.timedelta(days=180)).strftime("%d/%m/%Y"),
            'nights_in_dst_from' : 7,
            'nights_in_dst_to' : 28,
            'flight_type' : 'round',
            'limit' : 2,
            'curr' : 'GBP',
            'sort' : 'price',
            'price_to' : max_price
        }
        response = requests.get(url = self.search_url, params= query, headers= self.headers)
        try:
            data = response.json()['data'][0]
            #pprint(data)
        except IndexError:
            print(f"No flights found for {destination_code} from {dt.date.today().strftime('%d/%m/%Y')} to {(dt.date.today() + dt.timedelta(days=180)).strftime('%d/%m/%Y')}")
            return None

        flight_data = FlightData(
            price= data['price'],
            origin_city= data['cityFrom'],
            destination_city= data['cityTo'],
            origin_airport= data['flyFrom'],
            destination_airport= data['flyTo'],
            out_date=data['route'][0]['local_departure'].split('T')[0],
            return_date = data['route'][1]['local_departure'].split('T')[0]
        )
        print(f"Price: {flight_data.price} and destination: {flight_data.destination_city}")
        return(flight_data)



#flight = FlightSearch()
#flight.flight_search(origin_city='LON', destination_code= 'PAR')