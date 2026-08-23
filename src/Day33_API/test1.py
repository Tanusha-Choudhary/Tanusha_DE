import requests
import datetime
import smtplib
import time
my_email ="tnushachoudharry@gmail.com"
password = "kxwvcmciklyhnpcz"
MY_LAT=51.16
MY_LNG=-178.7504
def is_iss_overhead():
    parameters = {
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted":0,
    }
    response = requests.get("http://api.open-notify.org/iss-now.json",params=parameters)
    response.raise_for_status()
    data = response.json()
    # print(data)
    # 5:58:04 AM 7:19:46 PM
    iss_latitude = float(data["iss_position"]["latitude"])
    print(f"{iss_latitude}iss_latitude")
    iss_longitude = float(data["iss_position"]["longitude"])
    print(f"{iss_longitude}iss_longitude")
    print(f{MY_LAT}MY_LAT"")
    # your position in within +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return  True
is_iss_overhead()
def is_my_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.datetime.now()
    print(f"{time_now}time_now")
    print(f"{sunrise}sunrise")
    print(f"{time_now.hour}time_now.hour")
    print(f"{time_now.minute}time_now.minute")
    if time_now.hour >= sunrise and time_now.minute <= sunset:
        return True
is_my_time()
if is_iss_overhead() and is_my_time():
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login(my_email,password)
    connection.sendmail(from_addr=my_email,to_addrs=my_email,msg="subject:Look up\n\n The ISS is in the sky.")
    connection.close()
