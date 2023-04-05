##################### Extra Hard Starting Project ######################
import pandas
import smtplib
import datetime as dt
import random
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today_month_day = (now.month, now.day)
birthday_data = pandas.read_csv("birthdays.csv")
print(today_month_day)
for (index, row) in birthday_data.iterrows():
    birthday_data_tuple = (row.month, row.day)
    print(birthday_data_tuple)
    if today_month_day == birthday_data_tuple:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as letter_template:
            letter_contents = letter_template.read()
            updated_letter = letter_contents.replace("[NAME]", row["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            my_email = ""
            # make an app password in your Google account, and it is different from normal pass , 2 step must be active
            my_password = ""
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=row["email"],
                                msg=f"Subject:Happy Birth Day\n\n{updated_letter}")



# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




