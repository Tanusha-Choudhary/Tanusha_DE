
import smtplib
import datetime as dt
import random
from dataclasses import replace

my_email ="tnushachoudharry@gmail.com"
password = "rrnoktetfwevchwr"
now = dt.datetime.now()
# print(now.month)
list_f = {}
with open("friendlist","r") as f:
    list_of_friends = f.readlines()
    for i in list_of_friends:
        item1 = i.strip().split(" ")
        list_f[item1[0]] = item1[2]
    # print(list_of_friends)
    print(list_f)
for name,month in list_f.items():
    if now.month == 6 & int(month) ==6:
        with open('birthday_mail','r',encoding="utf-8") as f:
            mail_w = f.read()
            actual_mail = mail_w.replace("[name]", name)
            print(actual_mail)


#     print(ran_quote)
#
with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                    to_addrs="tnushachoudharry@gmail.com",
                    msg=f"Subject:Birthday Wishes \n\n{actual_mail}.".encode("utf-8"))
