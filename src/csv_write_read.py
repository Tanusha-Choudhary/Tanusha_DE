import csv
import json

rows = [["order_id","customer_id","amount","country"],
        [11,1,400,"USA"],
        [12,2,1000,"India"],
        [13,3,5000,"Japan"],
        [14,4,8000,"USA"]
        ]
# with open('orders.csv', 'w') as f:
#     # f.write("order_id,customer_id,amount,country\n")
#     for row in rows:
#         f.write("%s,%s,%s,%s\n" % (row[0],row[1],row[2],row[3]))
# # print("Done")

# with open('orders.csv', 'r',encoding="utf-8") as f:
#     print("Read entire file read() "
#           "or read(<fixed number of character>"
#           "or reading file using encoding)")
#     reader1 = f.read(10)
# print(reader1)
# with open('orders.csv', 'r') as f:
#     print("Read one line at a time ")
#     readerline1 = f.readline()
#     readerline2 = f.readline()
# print(readerline1)
# print(readerline2)
# with open('orders.csv', 'r') as f:
#     print("Read line by line, or read Large file ")
#     for line in f:
#         print(line.strip())
# print(reader1)
# import json
# with open("orders.json", "r") as f:
#     print("Read json file ")
#     orders = json.load(f)
# print(orders)
# with open("utils/tt", "rb") as f:
#     print("Read Binary file ")
#     image = f.read()
# print(type(image))
# TODO : check gzip again
# import gzip
# with gzip.open('utils/pong.zip', 'rt',encoding="utf-8") as f:
#     print("Read Compressed file")
#     reader1 = f.read()
# print(reader1)
# TODO excel file read using Pandas
# import pandas as pd
# df=pd.read_excel("utils/Book.xlsx")
# print(df)
# with open("orders.json", "r") as f:
#     print("Read json file ")
#     orders = json.load(f)
# print(orders)

# with open("orders.json", "r") as f:
#     print("Read files in chunks ")
#     while True:
#         chunk = f.read(1024)
#         if not chunk:
#             break
#         print(chunk)
import requests
print("Reading file from URL")
response = requests.get("https://www.linkedin.com/in/tanusha-choudhary/")
print(response.text)
