import requests
import os
from twilio.rest import Client

OPN_END = "https://api.openweathermap.org/data/2.5/onecall"

api_key = '******'



latitude = 23.825830
longitude = 78.734962
parameter  = {
'lat':latitude,
'lon':longitude,
'appid': api_key,
'exclude':"current,minutely,daily"
}

response = requests.get(OPN_END,params = parameter)
response.raise_for_status()
weather_data = response.json()
weather_slice =  weather_data['hourly'][:12]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700 :
        will_rain = True


       




# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "**********"
auth_token = "******"

if will_rain:
    print("Bring umbrella") 
    client = Client(account_sid, auth_token)    
    message = client.messages \
                    .create(
                        body="It's going to rain 💙",
                        from_='*********',
                        to='**********'
                    )

    print(message.status)