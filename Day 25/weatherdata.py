# with open("Day 25\weather_data.csv", 'r') as file:
#     data = file.readlines()
#     print(data)

import csv

import pandas

# with open("Day 25\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print (temperatures)


data = pandas.read_csv("Day 25\weather_data.csv")
print(data)
#print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# data_list = data["temp"].to_list() #This right here is a series as it is only calling one column, it is then converted to list

# print(data["temp"].mean())
# print(data["temp"].max())

# #Getting Data in Columns
# print(data["condition"])
# print(data.condition)

#Getting data in rows
#print(data[data.temp == data.temp.max()]) #So its data[row of temp column = temp max]

# monday = data[data.day == "Monday"]

# print(int(monday.temp) * 9/5 + 32)



#Create a dataframe from scratch
#Do pandas.Datafram("name of dict/list/etc.")
#data.to_csv("name of new file/folder")