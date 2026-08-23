try:
    amount ="100"
    f_amount= amount+10
    print("f_amount:",f_amount)
except TypeError:
    amount = "100"
    amount_n = int(amount)
    f_amount= amount_n+10
    # print(file_contents)
    print("Datatype issue found ")
    # print(file_contents)
finally:
    print("cleanup done bye")