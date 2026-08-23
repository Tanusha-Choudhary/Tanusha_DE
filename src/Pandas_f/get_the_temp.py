import pandas as pd
df = pd.read_csv("csv_file.csv")
df_temp = df["temperature_c"]
# print(type(df_temp))
# df_temp_1 = df[["temperature_c"]]
# print((df.temperature_c.max())*9/5 +32)
# print(df[df.temperature_c == df.temperature_c.max()])
# print(type(df_temp_1))
# df_avg = df_temp.mean()
# df_avg_1 = df_temp_1.agg("mean")
# print(df_avg_1)
# print(df_avg)

data_dict = {"students":["Anne","James","Angela"],
             "scores":[75,56,65]}
print(type(df.to_dict()))
data = pd.DataFrame(data_dict)
data.to_csv("csv_file1.csv")
