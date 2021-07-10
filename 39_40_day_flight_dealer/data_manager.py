import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/77a8bcd319a505608871956ed4407cc2/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/77a8bcd319a505608871956ed4407cc2/flightDeals/users"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.users_data = {}

    def get_destination_data(self):
   
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        #print(self.destination_data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)


    def get_users(self):
        response = requests.get(url = SHEETY_USERS_ENDPOINT)
        data = response.json()
        self.users_data = data["users"]
        #pprint(self.users_data)
        return self.users_data

    def update_data(self,first_name,last_name,email):
        info ={ "user" : {
            'email': email,
            'firstName': first_name,
            'lastName': last_name}
        }

        response = requests.post(url = SHEETY_USERS_ENDPOINT,json=info)
        #pprint(response.text)
        response = requests.get(url = SHEETY_USERS_ENDPOINT)
        data = response.json()
        self.users_data = data["users"]        
        return None

    def input_user(self):
        first_name = input("what is your first name? : ")
        last_name = input("what is your last name? : ")
        email = input("what is your email? : ")
        retype = input("Retype your email? :  ")
        if email != retype:
            self.input_user()
        self.update_data(first_name,last_name,email)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data            





        
   