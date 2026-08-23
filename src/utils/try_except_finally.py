# MISSING FILE HANDLING
try:
    with open("orders1.csv","r") as f:
        file_contents = f.read()
        # print(file_contents)
except FileNotFoundError:
    with open("/Users/tanushachoudhary/PycharmProjects/Tanusha_DE/src/orders.csv","r") as f:
        file_contents = f.read()
    # print(file_contents)
    # print("FILE NOT FOUND/pipeline can not be executed")
    # print(file_contents)
finally:
    print("cleanup done bye")