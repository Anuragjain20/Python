import requests
from twilio.rest import Client

twilio_account_sid = "ACab509a07dfcae"
twilio_auth_token = "a2327047eca"

STOCK = "IBM"
COMPANY_NAME = "IBM"
STOCK_API_KEY = "E7KIJI0B2434"
NEWS_API_KEY = "2432555555555"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'apikey':STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT,params=stock_params)



data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items() ]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday['4. close']

difference = (float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)
diff_percent = round((difference/float(yesterday_closing_price)) * 100)

print(diff_percent)
up_down = None
if difference > 0 :
    up_down = "🔺"
else:
    up_down= '🔻'
    

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if abs(diff_percent)> 0:
    print('get news')
    parameters = {'apiKey' : NEWS_API_KEY, 'qInTitle':COMPANY_NAME}
    news_response = requests.get(NEWS_ENDPOINT,params = parameters)
    articles =  news_response.json()['articles']
    three_articles = articles[:3]
  



    formatted_article = []

    for article in three_articles:
        formatted_article.append(f"{STOCK} : {up_down}{diff_percent}% \n Headline : {article['title']}. \n Brief: {article['description']} " )
    client = Client(twilio_account_sid, twilio_auth_token)    
    for article in formatted_article:
        message = client.messages \
                        .create(
                            body=article,
                            from_='********',
                            to='*****'
                        )








