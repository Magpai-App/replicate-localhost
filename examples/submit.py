import requests
import pprint

url = "http://localhost:5000/v1/predictions"
headers = {
    "Authorization": "Token NOT_A_REAL_TOKEN",
    "Content-Type": "application/json",
}
data = {
    "version": "r8.im/replicate/hello-world@sha256:5c7d5dc6dd8bf75c1acaa8565735e7986bc5b66206b55cca93cb72c9bf15ccaa",
    "input": {
        "text": "Magpai"
    },
}

response = requests.post(url, headers=headers, json=data)
pprint.pprint(response.json())
