import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USER_NAME = "somethingidk"
TOKEN = "tjwekwp939cwff"
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
running_graph_id = "test-graph"
graph_params = {
    "id": running_graph_id,
    "name": "Running Graph",
    "unit": "KM",
    "type": "float",
    "color": "shibafu",

}
headers = {
    "X-USER-TOKEN": TOKEN
}
today = datetime.now()
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
add_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{running_graph_id}"
add_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "7.2",
}
# response = requests.post(url=add_pixel_endpoint, json=add_pixel_params, headers=headers)
# print(response.text)
update_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{running_graph_id}/20220713"
update_pixel_params = {
    "quantity": "12.2",
}
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
# print(response.text)
response = requests.delete(url=update_pixel_endpoint, headers=headers)
print(response.text)
