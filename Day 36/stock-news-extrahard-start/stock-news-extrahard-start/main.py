STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
import requests
import datetime as dt
from datetime import timedelta
from twilio.rest import *
today = dt.date.today() - timedelta(days = 1)
yesterday = today - timedelta(days = 1)
apikey = 'Y90H3UY88LS9YMCM'
newsapi = 'a9b1f5efa3924ab8ab31fda5e786dd37'
parameters = {'function' : 'TIME_SERIES_DAILY_ADJUSTED',
              'symbol' : STOCK,
              'apikey' : apikey
              }
url = f'https://www.alphavantage.co/query'
r = requests.get(url, params= parameters)
data = r.json()["Time Series (Daily)"]

#Efficient Method (Theirs)
#data_list = [value for (key, value) in data.items()]
#yes = data_list[0]
#print(yes)

day_now_close = float(data[str(today)]['4. close'])
day_before_close = float(data[str(yesterday)]['4. close'])

calc = (day_now_close-day_before_close)/((day_now_close+day_before_close)/2)
#print(abs(calc))
#print(day_before_close)
#print(day_now_close)



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_param = {'q' : COMPANY_NAME,
              'from' : yesterday,
              'to' : today,
              'sortBy': 'relevancy',
              'apikey' : newsapi,
              'pageSize' : 3}

url2 = 'https://newsapi.org/v2/everything'

news = requests.get(url2, params = news_param)
articles = news.json()['articles']

account_sid = 'ACcc4158490acee5cd4a690e1726d12e9b'
auth_token = 'a7a2cfaa2c36f08520671bfe9581b69e'
client = Client(account_sid, auth_token)
## STEP 3: Use https://www.twilio.com





def message():
    for article in articles:
        if calc > 0:
            message = client.messages \
                        .create(
                            body=f"{STOCK}: 🔺{round(abs(calc) * 100, 2)}\nHeadline: {article['title']}\nBrief: {article['description']}\nURL: {article['url']}",
                            from_='+18337786829',
                            to='+18323405592'
                        )
        else:
            message = client.messages \
                        .create(
                            body=f"{STOCK}: 🔻{round(abs(calc) * 100, 2)}\nHeadline: {article['title']}\nBrief: {article['description']}\nURL: {article['url']}",
                            from_='+18337786829',
                            to='+18323405592'
                        )
                
if abs(calc) >= .00:
    message()
    print('done')

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

