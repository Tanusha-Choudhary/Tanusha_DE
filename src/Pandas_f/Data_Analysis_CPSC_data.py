from os import truncate

import pandas as pd
df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260604.csv")
# print(df.info())
# print(df[df["Primary Fur Color"] =="Gray"]["Primary Fur Color"].count())
# or
Gray_squirrels_count = len(df[df["Primary Fur Color"] =="Gray"])
Cinnamon_squirrels_count = len(df[df["Primary Fur Color"] =="Cinnamon"])
Black_squirrels_count = len(df[df["Primary Fur Color"] =="Black"])
# print(df[df["Primary Fur Color"] =="Cinnamon"]["Primary Fur Color"].count())
print(Gray_squirrels_count)
print(Cinnamon_squirrels_count)
print(Black_squirrels_count)
data_dict = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count": [Gray_squirrels_count,Cinnamon_squirrels_count,Black_squirrels_count]
}
print(data_dict)
pd.DataFrame(data_dict).to_csv("Count_of_squirrels.csv")