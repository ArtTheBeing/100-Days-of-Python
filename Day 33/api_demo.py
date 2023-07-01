import requests
import datetime as dt
#RESPONSE CODES
#1XX: Hold on
#2XX: Here you go
#3XX: Go away
#4XX: You screwed up/doesnt exists
#5XX: Problem Server Side
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# print(longitude)

parameters = {
    'lat': 51.507,
    'long': -.12277,
    'formatted' : 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']


time_now = dt.datetime.now()

#for i in range (len(time_now)):
    #if time_now[i]