import pandas

data = pandas.read_csv("Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#print(data)

fur = data["Primary Fur Color"]
new = pandas.DataFrame(fur.value_counts())
new.to_csv("Day 25/Fur")