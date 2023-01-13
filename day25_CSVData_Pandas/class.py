""" old ways
import csv

with open(".\day25_CSVData_Pandas\weather_data.csv", "r") as f:
    data = csv.reader(f)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
print(temperature) 
"""

import pandas as pd

data = pd.read_csv(".\day25_CSVData_Pandas\weather_data.csv")
data_list = data["temp"].tolist()

avg = data["temp"].mean()
max = data["temp"].max()
""" # avg = sum(data_list) / len(data_list)

# print(max) """

# get data from a column

""" 
# print(data["condition"])
# print(data.condition) """


# get data in Row

""" 
# print(data[data["day"] == "Monday"])
#print(data[data["temp"] == data["temp"].max()]) """


monday = data[data.day == "Monday"]
temp_f = (monday["temp"] * 9 / 5) + 32
print(temp_f)


# Create a dataframe from scratch:
data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}

dict_data = pd.DataFrame(data_dict)
dict_data.to_csv("new_data.csv")
