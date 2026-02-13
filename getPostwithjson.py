import requests
import json

url = "https://fakerestapi.azurewebsites.net"

head = {
    "accept": "text/plain",
    "Content-Type": "application/json"
}

json_file = open("./payload.json")
request_body = json.load(json_file)

response = requests.post(url+"/api/v1/Activities", headers=head, data=json.dumps(request_body))

print(response.text)
print("##############")
print(response.json())
