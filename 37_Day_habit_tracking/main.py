import requests
from datetime import datetime
pixela_endpoint =  "https://pixe.la/v1/users"
USERNAME = "g2011"
TOKEN = "9ksdue92e"
GRAPH_ID = "gh1"
user_pramas = {

    "token":TOKEN ,
    'username': USERNAME,
    'agreeTermsOfService':"yes",
    "notMinor":"yes"
}

#response = requests.post(url= pixela_endpoint, json=user_pramas)
#print(response.text)



graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Test",
    "unit":"hours",
    "type":"float",
    "color":"sora"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

#response = requests.post(url = graph_endpoint,json = graph_config,headers = headers)
#print(response.text)
#print(response.url)


pixel_creation_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()

pixel_data = {

    "date": today.strftime("%Y%m%d"),
    'quantity' : input("how many minutes did i code? " ),
}
response = requests.post(url = pixel_creation_endpoint,json=pixel_data,headers = headers)
print(response.text)

yesterday = datetime(year= 2021,month = 7,day = 5)
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity":"13",
}

#response = requests.put(url = update_endpoint,json=new_pixel_data,headers = headers)
#print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

#response = requests.delete(url =delete_endpoint,headers = headers)

#print(response.text)

