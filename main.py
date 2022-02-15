import smtplib
import datetime as dt
import random
import pandas

now = dt.datetime.now()
day = now.day
month = now.month
data = pandas.read_csv("birthdays.csv")
some_data = data.to_dict(orient='records')

for i in some_data:
    if day == i['day'] and month == i['month']:
        name = i['name']
        address_to_send = i['email']
        some_number = random.randint(1, 3)
        letter_to_use = f"letter_templates/letter_{some_number}.txt"
        with open(letter_to_use) as letter:
            letter_to_send = letter.read().replace("[NAME]", name)
            my_email = "blah.blah@gmail.com"    # email address from which message will be sent
            password = "password"               # password of above stated email address
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=address_to_send,
                    msg=f"Subject:Happy Birthday\n\n{letter_to_send}"
                )
