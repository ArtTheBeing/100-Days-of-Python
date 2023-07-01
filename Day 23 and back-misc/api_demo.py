import requests

#RESPONSE CODES
#1XX: Hold on
#2XX: Here you go
#3XX: Go away
#4XX: You screwed up/doesnt exists
#5XX: Problem Server Side
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
longitude = data["iss_position"]["longitude"]
print(longitude)