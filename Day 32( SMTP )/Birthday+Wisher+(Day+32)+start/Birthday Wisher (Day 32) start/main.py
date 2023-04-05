import smtplib
import datetime as dt

"""
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    my_email = ""
    # make an app password in your Google account, and it is different from normal pass , 2 step must be active
    my_password = ""
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="",
                        msg="Subject:Hello\n\nThis is the body of my email")
"""
"""
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(type(month), month)
date_of_birth = dt.datetime(year=1993, month=12, day=21, hour=3)
print(type(date_of_birth), date_of_birth)
"""
