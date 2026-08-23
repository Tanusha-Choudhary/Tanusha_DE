import csv

import pandas as pd
import matplotlib.pyplot as plt
# df = pd.read_csv("weathers.csv")
# print(df.head())
df = pd.DataFrame({"NAME":['tanvir k','NM  J','Asha Sharma','pravin kumar'],
                   "Age": [23,33,44,23],
                   "Sex":["male","male","female","male"],})
print(df.to_dict())
# # print(df.groupby(["Sex","Age"])["Age"].mean())
# print(df.value_counts())
# print(df)
# df.plot()
# plt.show()
# print(df.describe())
# print(df.dtypes)
# df.info()
# print(df["Age"].shape)
# print(df[df["Age"] > 33])
# print(df.filter(items =["Age"]))
# df.to_excel("weathers.xlsx",sheet_name="W1",index=False)
# df1 = pd.read_excel("weathers.xlsx",sheet_name="W1")
# print(df1)
# Getting data in to pandas from many different file formats or data sources is supported by read_* functions.
#
# Exporting data out of pandas is provided by different to_* methods.
#
# The head/tail/info methods and the dtypes attribute are convenient for a first check.
# with open("weathers.csv","r") as f1:
#     code1 = f1.readlines()
#     print(code1)
# with open("weathers.csv","r") as f2:
#     code2 = csv.reader(f2)
#     for i in code2:
#         print(i)
# df = pd.read_csv("weathers.csv")
# print(df)