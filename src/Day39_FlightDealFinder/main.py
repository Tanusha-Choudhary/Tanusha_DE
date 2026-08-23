import requests
parameter={
    "engine": "",
    "api_key": "",
    "departure_id":"",
    "arrival_id":"",
     "outbound_date":"",
    "type": ""}
response = requests.get("https://app.100daysofpython.dev",params=parameter)
data = response.text()
print(data)