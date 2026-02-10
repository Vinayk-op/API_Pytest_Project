import requests

# domain = "https://fakerestapi.azurewebsites.net/api/v1/Activities"
# Path = "/api/v1/Activities"
# url = domain + Path

head = {
    "accept": "text/plain",
    "Content-Type": "application/json"
}

request_payload = {
    "id": 121,
    "title": "Post Activity 2",
    "dueDate": "2024-06-30T00:00:00Z",
    "completed": True
}

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities",
                         headers=head, json=request_payload)

print(response.json())
print(response.status_code)

data = response.json()

assert response.status_code == 200
assert data["id"] == 121

