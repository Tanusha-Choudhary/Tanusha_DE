import smtplib,email
import subprocess
from email.message import EmailMessage
import requests

def ping_servers(serves):
    for server in serves:
        response = subprocess.call(f"ping -c 1 {server}", shell=True)
        if response == 0:
            print(f"Ping {server} successful")
        else:
            print(f"Ping {server} failed")
def send_mail(subject, content, to_email):
    your_email = "tanushachoudhary9999@gmail.com"
    password = "Sheena@1"
    msg = EmailMessage()
    msg.set_content(content)
    msg["Subject"] = subject
    msg["From"] = your_email
    msg["To"] = to_email
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(your_email, password)
    server.sendmail(msg)
    server.quit()
def api_check():
    response = requests.get("https://api.mailgun.net/v2/email//messages")
    print("initiated")
    if response.status_code == 200:
        data = response.json()
        print(data)
        print("Hurray")
    else:
        print ("alas")
    print("ended")
api_check()

# serves=["8.8.8.8", "8.8.4.4","192.168.1.1"]
# ping_servers(serves)
# send_mail("Reminder","Dont forget to call me!","tanushachoudhary1995@gmail.com")
