import requests
import pprint

url = "http://127.0.0.1:5000/v1/predictions"
headers = {
    "Authorization": "Token NOT_A_REAL_TOKEN",
    "Content-Type": "application/json",
}
data = {
    "version": "r8.im/magpai-app/cog-ffmpeg@sha256:efd0b79b577bcd58ae7d035bce9de5c4659a59e09faafac4d426d61c04249251",
    "input": {
        "command": "ffmpeg -version"
    },
}

response = requests.post(url, headers=headers, json=data)
if response.text:
    pprint.pprint(response.json())
else:
    print("Empty Response")