import requests
import os
from twilio.rest import Client
api_key = "85969cb0117c643b3eacdf4796ac67ba"
parameters = {'lat' : 29.519231,
              'lon' : -95.090689,
              'appid' : api_key
             }
data = requests.get("https://api.openweathermap.org/data/2.5/weather", params= parameters)
data = data.json()
current_weather = (data['weather'][0]['id'])
is_rain = False
account_sid = 'ACcc4158490acee5cd4a690e1726d12e9b'
auth_token = 'a7a2cfaa2c36f08520671bfe9581b69e'
client = Client(account_sid, auth_token)
if int(current_weather) < 750:
    is_rain = True
if is_rain:
    message = client.messages \
                .create(
                     body="Its goin to rain today! Brin an umbrella",
                     from_='+18337786829',
                     to='+18323405592'
                )
print(message.sid)