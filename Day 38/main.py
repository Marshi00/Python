import requests
from datetime import datetime
import os
NUTRITIONIX_API_ID = "2d3893d2"
NUTRITIONIX_API_KEY = os.environ["NUTRITIONIX_API_KEY"]
GSHEET_Endpoints = os.environ["GSHEET_Endpoints"]
# NUTRITIONIX_API_KEY = "eb36cc95d64f91a3cae9ffe70883b6c4"
# GSHEET_Endpoints = "https://api.sheety.co/66d9842fdc9d08ab839a3b358b0a25d8/workoutTracking/workouts"
Exercise_Endpoints = "https://trackapi.nutritionix.com/v2/natural/exercise"
TOKEN = "HakonaMatata923"
headers = {
    "x-app-id": NUTRITIONIX_API_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0"

}
exercise_params = {
    "query": input("Tell me which exercises you did "),
    "gender": "male",
    "weight_kg": 91,
    "height_cm": 184,
    "age": 28

}
today = datetime.now()
exercise_response = requests.post(url=Exercise_Endpoints, json=exercise_params, headers=headers)
print(exercise_response.text)
result = exercise_response.json()
print(result)
gsheet_headers = {
    "Authorization": f"Bearer {TOKEN}"
}
for item in result["exercises"]:
    sheet_params = {
        "workout": {
            "date": today.strftime("%d/%m/%y"),
            "time": today.strftime("%X"),
            "exercise": item["name"],
            "duration": item["duration_min"],
            "calories": item["nf_calories"],
        }
    }
    gsheet_response = requests.post(url=GSHEET_Endpoints, json=sheet_params, headers=gsheet_headers)
    print(gsheet_response.text)

# #Basic Authentication
# sheet_response = requests.post(
#   sheet_endpoint,
#   json=sheet_inputs,
#   auth=(
#       YOUR USERNAME,
#       YOUR PASSWORD,
#   )
# )
"""
# Returns `None` if key doesn't exist
print(os.environ.get('KEY_THAT_MIGHT_EXIST'))

# Returns `default_value` if key doesn't exist
print(os.environ.get('KEY_THAT_MIGHT_EXIST', default_value))

# Returns `default_value` if key doesn't exist
print(os.getenv('KEY_THAT_MIGHT_EXIST', default_value))
"""