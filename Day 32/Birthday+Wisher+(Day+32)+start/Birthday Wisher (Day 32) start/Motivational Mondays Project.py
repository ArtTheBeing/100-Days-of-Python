#Motivational Mondays Project

import smtplib
import datetime as dt
import random

my_email = "beingtheartist@gmail.com"
pword = "dhepuikazfiefypv"

with open("Day 32/Birthday+Wisher+(Day+32)+start/Birthday Wisher (Day 32) start/quotes.txt") as file:
    quotes = file.readlines()
    message = random.choice(quotes)


now = dt.datetime.now()
print(now.weekday())
if now.weekday() == 1:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #This line secures the connection and encrypts the email incase anyone sees it along its way
        connection.login(user=my_email, password= pword)
        connection.sendmail(from_addr =my_email, 
                            to_addrs= "dmccord9912@gmail.com", 
                            msg= f"Subject:Monday Motivation\n\n{message}")
        
