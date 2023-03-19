import requests

SHEETY_USERS_ENDPOINT = "https://api.sheety.co/66d9842fdc9d08ab839a3b358b0a25d8/flightDeals/users"
TOKEN = "HakonaMatata923"
gsheet_headers = {
    "Authorization": f"Bearer {TOKEN}"
}
print("Welcome to the Flight Club\nWe Find the best flight deals and email you.")
user_first_name = input("What is your first name : ")
user_last_name = input("What is your last name : ")
user_email = input("What is your email : ")
user_email_retype = input("please retype your email : ")
while user_email != user_email_retype:
    print("emails do not match.")
    user_email = input("What is your email : ")
    user_email_retype = input("please retype your email : ")
print("Welcome to the flight club")
new_user_data = {
    "user": {
        "firstName": user_first_name,
        "lastName": user_last_name,
        "email": user_email,

    }
}
response = requests.post(
    url=SHEETY_USERS_ENDPOINT,
    json=new_user_data,
    headers=gsheet_headers
)
print(response.text)
