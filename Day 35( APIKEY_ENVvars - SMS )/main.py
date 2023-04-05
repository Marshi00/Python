import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
# trying with server run
# 1
# proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
# 2
# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {'https': os.environ['https_proxy']}
twilio_account_sid = os.environ.get('twilio_account_sid')
twilio_auth_token = os.environ.get('twilio_auth_token')
# twilio_account_sid =''
# twilio_auth_token = ''
MY_NUMBER = '+'
MY_LAT = 43.653225  # Your latitude
MY_LONG = -79.383186  # Your longitude
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": "",
    "exclude": "daily,minutely,current"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
print(response.status_code)
response.raise_for_status()
weather_data = response.json()
next_twelve_hours_data = weather_data["hourly"][:12]
next_twelve_hours_data_weather = [item["weather"] for item in next_twelve_hours_data]
need_umbrella = False
for hour_data in next_twelve_hours_data_weather:
    condition_code = int(hour_data[0]["id"])
    if condition_code < 700:
        need_umbrella = True

if 1 == 1:
    client = Client(twilio_account_sid, twilio_auth_token)
    # for server run
    # client = Client(twilio_account_sid, twilio_auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today, Remember to bring an umbrella.",
        from_=MY_NUMBER,
        to='+15194041210'
    )
    print(message.sid)
    print(message.status)
# and set the environment variables. See http://twil.io/secure
# set up Proxy connect and test sms coming + env set up
