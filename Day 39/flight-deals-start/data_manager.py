import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/66d9842fdc9d08ab839a3b358b0a25d8/flightDeals/prices"
TOKEN = "HakonaMatata923"
gsheet_headers = {
    "Authorization": f"Bearer {TOKEN}"
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=gsheet_headers)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"],
                    # Updating lowest price as well, testing
                    # "lowestPrice": city["lowestPrice"]

                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=gsheet_headers
            )
            print(response.text)
