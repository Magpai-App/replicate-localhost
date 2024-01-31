import requests
import pprint

PREDICTION_ID = "REPLACE_ME"

url = "http://127.0.0.1:5000/v1/predictions/" + PREDICTION_ID
headers = {
    "Authorization": "Token NOT_A_REAL_TOKEN",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
if response.text:
    pprint.pprint(response.json())
else:
    print("Empty Response")