import requests

head = {
    "accept": "text/plain",
    "Content-Type": "application/json"
}

get_response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/13", headers=head)

print("Before Update:", get_response.json())

request_payload = {
  "id": 133,
  "title": "VK updated through requests",
  "dueDate": "2026-02-11T18:01:23.569Z",
  "completed": True
}

put_response = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/13", headers=head, json=request_payload)

print("After update:", put_response.json())