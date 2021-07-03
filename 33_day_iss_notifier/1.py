import requests

response = requests.get(url = "http://api.open-notify.org/iss-now.json")


response.raise_for_status()

data = response.json()
print(data)
print("\n\n\n")

MY_LAT = 51.507351
MY_LONG = -0.127758

parameters = {
    'lat':MY_LAT,
    'lng' :MY_LONG,
    'formatted':0
}

response = requests.get(url= "https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]['sunrise'].split('T')[1].split(':')[0])
sunset = int(data["results"]['sunset'].split('T')[1].split(':')[0])

