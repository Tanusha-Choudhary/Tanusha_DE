import requests
BASE_URL="https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
APP_ID="app_976c6f69aa854a9ab4fbd6e8"
API_KEY="nix_live_7QVsR7gL8OAWa3MAIbuMAlk183dAvZfm"
GENDER="female"
WEIGHT_KG=58
HEIGHT_CM=180
AGE = 38
headers = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY
}
params ={
  "query": "swam for 1 hour",
  "gender": GENDER,
  "weight_kg": WEIGHT_KG,
  "height_cm": HEIGHT_CM,
  "age": AGE
}
response = requests.post(BASE_URL,json=params,headers=headers)
result = response.json()
print(result)
