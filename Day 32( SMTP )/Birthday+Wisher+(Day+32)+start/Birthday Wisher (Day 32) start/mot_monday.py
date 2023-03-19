import pandas
import smtplib
import datetime as dt
import random

now = dt.datetime.now()
if now.weekday() == 0:
    with open("quotes.txt", "r") as quotes:
        quotes_list = quotes.readlines()
        mot_quote = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        my_email = "mo.arshian00@gmail.com"
        # make an app password in your Google account, and it is different from normal pass , 2 step must be active
        my_password = "nmlhyatkgswntemn"
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="arshiyan.mohammad48@gmail.com",
                            msg=f"Subject:Hello\n\n {mot_quote}")


