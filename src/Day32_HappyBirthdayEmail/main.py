import pandas as pd
import smtplib
from datetime import datetime as dt
import random
from dataclasses import replace
today_tuple = (dt.now().day,dt.now().month)
# print(today_tuple)
my_email ="xyz@gmail.com"
password = "password"
# print(now.month)
pd = pd.read_csv("friendlist",sep=" ")
dictionary_date = { (data_row["day"],data_row["month"]):data_row for (index,data_row) in pd.iterrows()}
# print(dictionary_date)
# for i in dictionary_date:
#     print(i)
if today_tuple in dictionary_date:
    birthday_name = dictionary_date[today_tuple]
    # print(birthday_name["name"])
    with open('birthday_mail','r',encoding="utf-8") as f:
            mail_w = f.read()
            actual_mail = mail_w.replace("[name]", birthday_name["name"])
            # print(actual_mail)
#
with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                    to_addrs="tnushachoudharry@gmail.com",
                    msg=f"Subject:Birthday Wishes \n\n{actual_mail}.".encode("utf-8"))
