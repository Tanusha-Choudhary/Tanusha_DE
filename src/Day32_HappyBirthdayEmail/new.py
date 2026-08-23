# smtplib
# Gmail: smtp.gmail.com
import smtplib
import datetime as dt
import random
my_email ="tnushachoudharry@gmail.com"
password = "rrnoktetfwevchwr" #Generate in your GmailAccount-> Profile-> Security-> AppPassword->passwordSection
now = dt.datetime.now()
# now = dt.datetime(year=2021,month=8,day=17,hour=23,minute=59,second=59)
week_day = now.weekday()
print(week_day)
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# with open('quotes.txt','r') as f:
#     updated_records=[]
#     quotes = f.readlines()
#     for i in quotes:
#         updated_records.append((i.split('.')[1]).strip())
#     ran_quote = random.choice(updated_records)
    # print(quotes)

with open('quotes.txt','r') as f:
    quotes = f.readlines()
    ran_quote = random.choice(quotes)
    print(ran_quote)

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                    to_addrs="tnushachoudharry@gmail.com",
                    msg=f"Subject:Hello Love\n\n{ran_quote}.")
