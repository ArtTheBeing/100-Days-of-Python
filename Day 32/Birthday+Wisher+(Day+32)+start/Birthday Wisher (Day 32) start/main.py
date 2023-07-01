# import smtplib

# my_email = "beingtheartist@gmail.com"
# pword = "dhepuikazfiefypv"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls() #This line secures the connection and encrypts the email incase anyone sees it along its way
#     connection.login(user=my_email, password= pword)
#     connection.sendmail(from_addr =my_email, 
#                         to_addrs= "dmccord9912@gmail.com", 
#                         msg= "Subject:Hello\n\nThis is the body of my email")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
print(now)

date_of_birth = dt.datetime(year = 2004 , month = 4 , day = 13)
print(date_of_birth)