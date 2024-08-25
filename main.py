import smtplib
import datetime as dt
import random
import csv


now = dt.datetime.now()
current_day = now.day
current_month = now.month
current_year = now.year
my_email = "luifer3008@gmail.com"
password = "xlkzgxuoeccbpnfr"

with open('birthdays.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        name = row[0]
        email = row[1]
        year = int(row[2])
        month = int(row[3])
        day = int(row[4])

        if month == current_month and day == current_day:
            letter_n = random.randint(1,3)
            with open(f'letter_templates/letter_{letter_n}.txt', mode='r') as letter_to_modify:
                content = letter_to_modify.read()
                modified_content = content.replace("[NAME]", name)
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=email,
                                    msg=f"Subject:Happy {current_year - year} Birthday {name}!\n\n{modified_content}")