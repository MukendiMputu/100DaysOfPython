import pandas as pd
# # import statistics as stat
#
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# # print(data_dict)
#
# # temp_list = data.temp.to_list()
# temp_list = data["temp"].to_list()
# # print(temp_list)
#
# # Series.mean()
# avg_temp = data["temp"].mean()
# # avg_temp = stat.mean(temp_list)  # sum(temp_list) / len(temp_list)
# # print(avg_temp)
# # print(data["temp"].max())
#
# # Get Row
# print(data.temp[data.temp == data.temp.max()])

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Data.csv")
# print(squirrel_data)

total_count = len(squirrel_data["Primary Fur Color"])
gray = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

fur_dict = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Amount": [gray, cinnamon, black],
    "Total count": total_count
}

data_frame = pd.DataFrame(fur_dict)
data_frame.to_csv("squirrel_count.csv")

print(fur_dict)
