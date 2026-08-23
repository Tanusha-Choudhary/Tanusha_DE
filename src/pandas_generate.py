import pandas as pd
df = pd.DataFrame({"order_id":range(1,11),
                   "amount":[45,None,56,77,88,None,99,80,45,23],
                   "country":['US','IN','US','US','IN','US','IN','US','US','IN']}
                  )
# df.to_csv("orders.csv",index=False)
# print(df)
df["running_total"]= df["amount"].cumsum()
# print(df)
