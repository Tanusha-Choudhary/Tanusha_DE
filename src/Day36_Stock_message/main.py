import requests
import twilio
from twilio.rest import Client
STOCK_NAME ="TSLA"
COMPANY_NAME ="Tesla Inc."
NEWS_API_KEY ="a573fbb1b23549288612e634ac3788c4"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=RELIANCE.BSE&outputsize=full&apikey=demo
STOCK_API = "UFJ57CLWAEOZIKWT"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
# print(data)
data_list = [values for key,values in data.items()]
#TODO 1:- Get yesterday's closing stock price
yesterday_data=data_list[0]["4. close"]
#TODO:2 - Get the day before yesterday's closing stock price
day_before_yesterday=data_list[1]["4. close"]
print(yesterday_data)
print(day_before_yesterday)
#TODO-3 : Find the positive difference between 1 and 2 e.g. 40-20 = -20 but the positive difference is 20 :
difference=float(yesterday_data) - float(day_before_yesterday)
if difference > 0:
    up="🔺"
else:
    down="🔻"

#TODO 4:- Work out the value of 5% of yesterday's closing price
difference_per = round((float(difference)/float(yesterday_data) )* 100)
#TODO:5 - If TODO4 is true then print("get News")
if abs(difference_per)>2:
    news_params = {
        'apiKey': NEWS_API_KEY,
        'qInTitle': COMPANY_NAME,
    }
    print("Get News")
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    three_articles = response.json()["articles"][0:3]
# TODO-6 - Using python get first 3 articles's headline  and description using list comprehension
    formatted_articles = [f"{STOCK_NAME}:{up}{difference}%\nHeadlines:{article['title']}.\n Brief: {article['description']}" for article in three_articles]
    account_sid = 'AC3940091ea68f2470237280e54ca7d626'
    auth_token = '5834bca84da4fc8c437f6b3243ce5cb4'
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=article,
            to='whatsapp:+918889832307'
    )
    print(message.sid)

    # print(three_articles)
# print(difference_per)

