import requests
import datetime
import smtplib
import time
my_email ="tnushachoudharry@gmail.com"
password = "kxwvcmciklyhnpcz"
MY_LAT=18.520430
MY_LNG=73.856743
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
    print(iss_latitude)
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_longitude)
    # your position in within +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return  True
# is_iss_overhead()
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
    if time_now.hour >= sunrise and time_now.minute <= sunset:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_my_time():
        connection = smtplib.SMTP('smtp.gmail.com', 587)
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg="subject:Look up\n\n The ISS is in the sky.")
        connection.close()
