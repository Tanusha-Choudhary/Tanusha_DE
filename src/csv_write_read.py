import csv
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
# print("Done")
# with open('orders.csv', 'r') as f:
#     reader = f.readlines()
#     print(reader)
# print("Done")
with open('orders.csv', 'r') as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)
# print("Done")