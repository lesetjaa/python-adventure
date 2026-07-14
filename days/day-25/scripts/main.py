# TODO - Open the weather_data.csv file. Use .readline() to create a list of named data that contains the values fro. the csv file.

# with open("../resources/weather_data.csv", mode="r") as file:
#     data = file.readlines()

# import csv

# with open("../resources/weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)

#     # TODO. - Extract all of the temp
#     temperatures = []

#     for row in data:
#         if row[1] != "temp":
#             weather_temp = row[1]
#             temperatures.append(int(weather_temp))

#     print(temperatures)
#     # for row in data:
#     #     print(row)

import pandas

data = pandas.read_csv("../resources/weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# # TODO - Calculate the averge temperature

# average = data["temp"].mean()
# print(average)

# # TODO - Get the maximum value by using the one of the data Series methods

# max_value = data["temp"].max()
# print(max_value)

# print(data[data.day == "Monday"])

# # TODO - Print the row of data which had the highest temperature

# highest_temp = data["temp"].max()
# print(data[data.temp == highest_temp])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# TODO - Convert Monday's temperature to Fahrenheit.


def celcius_to_fahrenheit(temp_in_cel):
    return (temp_in_cel * 9/5) + 32


monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = celcius_to_fahrenheit(monday_temp)

print(monday_temp_F)

data_dict = {
    "student": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("../resources/new_data.csv")
