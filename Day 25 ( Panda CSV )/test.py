import csv
import pandas

"""
with open("weather_data.csv", mode="r") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if not row[1] == "temp":
            temperatures.append(int(row[1]))

    print(temperatures)
"""
"""
data = pandas.read_csv("weather_data.csv")
print(data["temp"])

# Get data in columns
print(data["condition"])
print(data.condition)
# Get data in rows
print(data[data.day == "Wednesday"])
print(data[data.temp == data["temp"].max()])

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "Joe", "David"],
    "score": [40, 49, 41]
}
data_frame = pandas.DataFrame(data_dict)
print(data_frame)
# Making CSV
data_frame.to_csv("new_Data.csv")
"""
# Central_Park_DATA
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_data = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_data = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_data = len(data[data["Primary Fur Color"] == "Black"])
central_park_data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_data, Cinnamon_data, Black_data]
}
central_park_data_frame = pandas.DataFrame(central_park_data_dict)
central_park_data_frame.to_csv("central_park.csv")
