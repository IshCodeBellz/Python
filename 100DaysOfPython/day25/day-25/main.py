# with open("weather_data.csv") as weather:
#     data = weather.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as weather:
#     data = csv.reader(weather)
#     temperatures = []
#     print(data)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# # print(len(temp_list)
# total = 0
# print(temp_list)
# # for temp in temp_list:
# #     total = total + temp
# # print(int(total/len(temp_list)))
#
# # average = sum(temp_list)/len(temp_list)
# # print(average)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data["condition"])
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
# # f_temp = int(monday.temp) * (9/5) + 32
# f_temp = int(monday.temp.iloc[0]) * (9/5) + 32
#
# print(f_temp)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# my method
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# temp_list = data["Primary Fur Color"].to_list()
#
# grey = 0
# red = 0
# black = 0
#
# for color in temp_list:
#     if color == "Gray":
#         grey += 1
#     elif color == "Cinnamon":
#         red += 1
#     elif color == "Black":
#         black += 1
#     else:
#         continue
# print(grey, red, black)
# data_dict = {
#     "Fur Color": ["grey", "red", "black"],
#     "Count": [f"{grey}", f"{red}", f"{black}"]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("squirrel_count.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# temp_list = data["Primary Fur Color"].to_list()
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")
