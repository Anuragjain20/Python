import smtplib
import datetime as dt
import random

MY_EMAIL =  'arjfootball07@gmail.com'
MY_PASSWORD = 'Anurag11@'
reciver = 'arjfootball07@gmail.com'
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with  smtplib.SMTP_SSL('smtp.gmail.com')as connection:

        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = reciver,
            msg = f'Subject: Monday Motivation\n\n{quote}'       
        
        )