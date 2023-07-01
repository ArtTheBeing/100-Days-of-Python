##################### Normal Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib
today = dt.datetime(year=2023, month=4, day=13)
today = (today.month, today.day)

data = pandas.read_csv("Day 32/birthday-wisher-extrahard-start/birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}


#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"Day 32/birthday-wisher-extrahard-start/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person['name'] )
    my_email = "beingtheartist@gmail.com"
    pword = "dhepuikazfiefypv"
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password= pword)
        connection.sendmail(from_addr =my_email, 
                            to_addrs= birthday_person['email'], 
                            msg= f"Subject:Happy Birthday!\n\n{contents}"
                            )




