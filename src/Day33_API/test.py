import requests
response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_positio = (longitude, latitude)
print(iss_positio)
# if response.status_code ==404:
#     raise Exception("Not Found")
# elif response.status_code ==401:
#     raise Exception("Unauthorized")

# print(response) , Output : <Response [200]>
