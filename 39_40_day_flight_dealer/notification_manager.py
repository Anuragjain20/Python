from twilio.rest import Client
import smtplib
TWILIO_SID = "ACab509a07dfca6"
TWILIO_AUTH_TOKEN = "a2327047eca6f8d1e573"
TWILIO_VIRTUAL_NUMBER = '+14157'
TWILIO_VERIFIED_NUMBER = '+******'
MY_EMAIL =  'arjfootball07@gmail.com'
MY_PASSWORD = '***********'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)


    def send_emails(self, emails, message, google_flight_link):
        with  smtplib.SMTP_SSL('smtp.gmail.com') as connection:
    
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )