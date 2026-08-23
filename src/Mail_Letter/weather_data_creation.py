import csv

data = [
    ["day", "temp", "condition"],   # header
    ["Monday", 25, "Sunny"],
    ["Tuesday", 22, "Rainy"]
]

with open("weathers.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
#
# print("CSV file created")
# with open("weathers.csv","r") as f1:
#     content = f1.readlines()
#     print(content)
with open("weathers.csv","r") as f1:
    code1 = csv.reader(f1)
    # print(code1)

    temperature = []
    # # print(code1)
    for row in code1:
        if row[1] != "temp":
            temperature.append(int(row[1])) # use pandas
        print(row)
    print(temperature)
