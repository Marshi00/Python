import requests
import lxml
from bs4 import BeautifulSoup
from notification_manager import NotificationManager

notification_manager = NotificationManager()
URL = "https://www.amazon.com/HP-24mh-FHD-Monitor-Built/dp/B08BF4CZSV/ref=lp_16225007011_1_11"
# You can see your browser headers by going to this website:
#
# http://myhttpheader.com/
amazing_web_page_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77",
    "Accept-Language": "en-US,en;q=0.9",
}
response = requests.get(url=URL, headers=amazing_web_page_headers)
amazon_web_page = response.text
soup = BeautifulSoup(amazon_web_page, "lxml")

item_price = soup.find(name="span", class_="a-offscreen").getText()
print(item_price.split("$")[1])
# movie_titles = [title.getText() for title in titles]
item_price2 = soup.select_one(selector="span .a-offscreen").getText()
print(item_price2)
current_price = float(item_price.split("$")[1])
if current_price < 200:
    message = f"Low price alert! Only ${current_price} for the HP Screen ."
    emails = ["mo.arshian00@gmail.com"]
    notification_manager.send_emails(emails=emails, message=message, link=URL)
