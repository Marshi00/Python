import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# from newsapi import NewsApiClient
MY_NUMBER = '+19897122708'
twilio_account_sid = 'AC79bbcb586907bdaf95747e945d38e169'
twilio_auth_token = '712b5db344c175e07a85c4dca1061cce'
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
FUNCTION = "TIME_SERIES_DAILY"
alphavantage_Daily_api_key = "H63BTTF2COUFI489"
newsapi_api_key = "9a47ef2aad794d908c9c9cdfccae1fbb"
alphavantage_Daily_parameters = {
    "function": FUNCTION,
    "symbol": STOCK,
    "apikey": alphavantage_Daily_api_key,
    "outputsize": "compact"
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alphavantage_Daily_api_key_response = requests.get("https://www.alphavantage.co/query",
                                                   params=alphavantage_Daily_parameters)
print(alphavantage_Daily_api_key_response.status_code)
alphavantage_Daily_api_key_response.raise_for_status()
stock_data = alphavantage_Daily_api_key_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]
stock_date_list = [key for (key, value) in stock_data.items()][0:2]
print(stock_date_list[0], stock_date_list[1])
last_two_days_closing_stock_data = stock_data_list[0:2]
print(float(stock_data_list[0]["4. close"]), float(stock_data_list[1]["4. close"]))
last_two_days_stock_data_difference_percent = (abs(float(stock_data_list[0]["4. close"]) - float(
    stock_data_list[1]["4. close"])) / float(stock_data_list[0]["4. close"])) * 100
up_down = ""
if float(stock_data_list[0]["4. close"]) - float(stock_data_list[1]["4. close"]) < 0:
    up_down = "⬇️"
else:
    up_down = "⬆️"
if last_two_days_stock_data_difference_percent >= 2:
    print("Get News", f"the percent difference is {round(last_two_days_stock_data_difference_percent, 2)} ")
    newsapi_api_key_parameters = {
        "q": STOCK,
        "from": stock_date_list[1],
        "apiKey": newsapi_api_key,
        "sortBy": "relevancy",
        "to": stock_date_list[0],
    }
    ## STEP 2: Use https://newsapi.org

    newsapi_api_key_response = requests.get("https://newsapi.org/v2/everything",
                                            params=newsapi_api_key_parameters)
    print(newsapi_api_key_response.status_code)
    newsapi_api_key_response.raise_for_status()
    news_data = newsapi_api_key_response.json()['articles']
    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    three_articles = news_data[0:3]
    articles_list = [
        f"{STOCK}: {up_down} , the percent difference is {round(last_two_days_stock_data_difference_percent, 2)} %, " \
        f"Headline:{value['title']}.\nBrief:{value['description']} "
        for value in
        three_articles]
    client = Client(twilio_account_sid, twilio_auth_token)
    for article in articles_list:
        message = client.messages \
            .create(
            body=article,
            from_=MY_NUMBER,
            to='+15194041210'
        )
        print(message.sid)
        print(message.status)
# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
