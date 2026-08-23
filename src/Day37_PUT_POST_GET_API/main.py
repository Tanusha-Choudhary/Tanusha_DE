import requests
from datetime import datetime
pixela_endpoint ="https://pixe.la/v1/users"
USERNAME = "tanusha"
TOKEN ="werereefdfef"
GRAPH_ID="graph1"
user_params = {
    "token": TOKEN ,
    "username": USERNAME ,
    "agreeTermsOfService": "yes",
    "notMinor" : "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN":TOKEN
}
# TODO: GRAPH CREATION
# response=requests.post(url=graph_endpoint, json=graph_config,headers=headers)
# print(response.text)
pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
TODAYS_DATE = datetime.now()
# TODAYS_DATE= datetime(year=2026, month=7, day=18)
# print(TODAYS_DATE)
pixel_data = {
    "date": TODAYS_DATE.strftime("%Y%m%d"),
    "quantity": input("How many Km I have run"),
}
# TODO:POST
# response = requests.post(pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)
upload_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAYS_DATE.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "3.3",
}
# TODO:PUT
# response = requests.put(url=upload_endpoint, json=pixel_data, headers=headers)
# print(response.text)
# TODO:DELETE
delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAYS_DATE.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)