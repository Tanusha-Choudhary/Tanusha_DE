import pandas as pd
df1 = pd.read_csv("orders.csv")
df1["amount"]=df1["amount"].fillna(0).astype(int)
df1["country"]=df1["country"].str.upper()
print(df1)
country_summary=(df1.groupby("country").agg(total_order = ("order_id", "count")
                                            ,total_amount = ("amount", "sum")
                                            ))
print(country_summary)