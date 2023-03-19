import requests
from flight_data import FlightData
from pprint import pprint

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "Q_jrfcLVRNU09zLDps5OTQSp98vDVLuu"
TEQUILA_HEADER = {
    "apikey": TEQUILA_API_KEY,
}


class FlightSearch:
    def __init__(self):
        self.query = {
            "locale": "en-US",
            "location_types": "city",
            "active_only": "true",
            "term": ""
        }

    def get_destination_code(self, city_name):
        self.query["term"] = city_name
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=self.query, headers=TEQUILA_HEADER)
        data = response.json()["locations"]
        code = data[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "CAD"
        }
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )
        try:
            data = response.json()["data"][0]
            print(f"{destination_city_code} {data['price']}")

        except IndexError:
            print(f"No Direct flights found for {destination_city_code}.")
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers,
                params=query,
            )
            try:
                data = response.json()["data"][0]
                print(f" 1 stop flight found for {destination_city_code} {data['price']}")
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                return flight_data
            except IndexError:
                print(f"No  flights found for {destination_city_code}.")
                return None
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
            )
            print(f"{flight_data.destination_city}: ${flight_data.price}")
            return flight_data
