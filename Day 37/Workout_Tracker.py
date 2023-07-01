#Workout Tracker
import requests
import datetime as dt
nutrionx_api = '053b9a628e5014145dc595f8e62046f3'
nutrionx_appid = '12bc86ea'
#workout = input("Tell me about your workout: ")
workout= "i ran 3 miles"
headers = {'x-app-id' : nutrionx_appid,
           'x-app-key' : nutrionx_api}

exercise_params = {
    'query' : str(workout),
    'gender' : 'male',
    'weight_kg' : 78,
    'height_cm' : 176,
    'age' : 19
}

post_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

response = requests.post(url= post_url, json= exercise_params, headers=headers)
print(response.text)

exer = (response.json()['exercises'][0]['user_input'])
dur = (response.json()['exercises'][0]['duration_min'])
cal = (response.json()['exercises'][0]['nf_calories'])
print(exer)

sheety_url = 'https://api.sheety.co/344c69e7d5b351a6b79f3543079fe62d/copyOfMyWorkouts/workouts'

google_params = {
    'workout' : {
        'date' : str(dt.datetime.today().strftime('%d/%m/%Y')),
        'time' : str(dt.datetime.now().strftime('%H:%M:%S')),
        'exercise' : str(exer).title(),
        'duration' : str(dur),
        'calories' : cal,

    }
}

headers = {'Bearer' : 'ksajdfehfhaswqad'}

response = requests.post(url = sheety_url, json= google_params, headers=headers)
print(response.text)

