##################### Extra Hard Starting Project ######################
import random
# 1. Update the birthdays.csv
global their_email
# 2. Check if today matches a birthday in the birthdays.csv
import datetime as dt
import pandas
now = dt.datetime(year = 2023, month= 4, day= 13)
data = pandas.read_csv("Day 32/birthday-wisher-extrahard-start/birthdays.csv")
#print(data)
name_letter = ""
for i in range(len(data)):
    row = data.loc[i]
    if row.month == now.month and row.day == now.day:
        their_email = row.email
        name_letter = row['name']
    

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        message = ""
        with open(f"Day 32/birthday-wisher-extrahard-start/letter_templates/letter_{random.randint(1,3)}.txt") as directory:
            lines = directory.readlines()
            for val in lines:
                if "[NAME]" in val:
                    val = val.replace("[NAME]", name_letter)
                message += val


# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
try:
    print(their_email)
    my_email = "beingtheartist@gmail.com"
    pword = "dhepuikazfiefypv"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #This line secures the connection and encrypts the email incase anyone sees it along its way
        connection.login(user=my_email, password= pword)
        connection.sendmail(from_addr =my_email, 
                            to_addrs= their_email, 
                            msg= f"Subject:Happy Birthday!\n\n{message}"
                            )

except NameError:
    print("No birthdays today")






