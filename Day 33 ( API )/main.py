import requests
from datetime import datetime

MY_LAT = 43.653225
MY_LONG = -79.383186
"""
Response codes
1XX : Hold On
2XX : Here Yoy Go
3XX : GO Away, No Permission 
4XX : You Screwed Up, Something Wrong ( Doesn't Exist ) 
5XX : Server Screwed Up

"""
"""
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)

print(data)
print(iss_position)
"""
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise_hour = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_hour = data["results"]["sunset"].split("T")[1].split(":")[0]
time_now = datetime.now()
print(data)
print(time_now)
