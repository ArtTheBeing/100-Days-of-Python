#HTTP REQUESTS - Get Request, Post Request, Put Requests, Delete REquests
#requests.get() - Gets information
#requests.post() - Send data, recieve info on whether your data went through or not
#requests.put() - Updata sent data
#requests.delete() - Delete some information you have sent

TOKEN = 'fghdasheahfajhfe'
USERNAME = 'dannydymes'
GRAPHID = 'graph1'
import datetime as dt
import requests
pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    'token' : TOKEN,
    'username' : USERNAME,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes',

}

# response = requests.post(url = pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id': GRAPHID,
    'name': 'Coding Graph',
    'unit': 'projects',
    'type': 'int',
    'color' : 'ajisai'
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

#response = requests.post(url = graph_endpoint, json= graph_config, headers=headers)
#print(response.text)


#--------------------DATA CREATION----------------------

today = str(dt.date.today()).replace('-','')
quantity = input("How many projects?: ")

pixel_post = {
    'date' : today,
    'quantity': quantity
}

response = requests.post(url = f"{graph_endpoint}/{GRAPHID}", json = pixel_post, headers=headers)
print(response.text)


#---------------UPDATER---------------

# update_endpoint = f"{graph_endpoint}/{GRAPHID}/{today}"
# quantity = input("How many projects?: ")
# update_data = {
#     'quantity' : quantity
# }

#requests.put(url = update_endpoint, json= update_data, headers=headers)