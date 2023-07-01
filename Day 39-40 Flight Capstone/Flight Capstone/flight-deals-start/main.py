from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

flight_search = FlightSearch()
data = DataManager()

#-------------------------------------------# Functions
def new_iata(list):
    for (key,val) in list.items():
        for info in sheet_data:
            if info['city'] == key:
                info['iataCode'] = val





sheet_data = data.get_info()
print(shee)
pass_list = [info['city'] for info in sheet_data]
#print(pass_list)
# my_dict = {}
# for item in pass_list:
#     my_dict[item] = flight_search.destination_code(item)


#new_iata(my_dict)
#pprint(sheet_data)

#data.update(sheet_data)

for i in range(len(data.get_info())):
    price_check = data.get_info()[i]['lowestPrice']
    destination = data.get_info()[i]['iataCode']
    print(flight_search.flight_search('LON', destination, price_check))

