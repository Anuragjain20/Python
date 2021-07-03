import smtplib
from datetime import datetime
import pandas as pd
import random
today = datetime.now()
today_tuple = (today.month,today.day)
MY_EMAIL =  'arjfootball07@gmail.com'
MY_PASSWORD = 'abc'

data = pd.read_csv('birthday.csv')
#print(today_tuple)

birthday_dict = {(data_row['month'] , data_row['day']) : data_row for (index,data_row) in data.iterrows()}
#print(birthday_dict)
if today_tuple in birthday_dict:
    birthday_person  = birthday_dict[today_tuple]
    file_path = f'letter{random.randint(1,2)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        content = contents.replace('[Name]',birthday_person['name'])
        #print(content)
        #print(birthday_person['email'])

    with  smtplib.SMTP_SSL('smtp.gmail.com')as connection:

        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = birthday_person['email'],
            msg = f'Subject: Happy Birthday\n\n{content}'       
        
        )