import requests

url = "https://gorest.co.in/public/v2/users"

head = {
    "accept": "application/json",
    "Authorization": "Bearer 5a1586548bc1a6e5de301f97805771be184c3e29d6a616c5056681c27f407e9b"
}

request_payload = {
    "name": "Vinay 12345",
    "email": "vkg1234@gmail.com",
    "gender": "male",
    "status": "active"
}

response = requests.post(url, headers=head, json=request_payload)

print(response.json())
assert response.status_code == 201

response = requests.get(url+"/"+str(response.json()["id"]), headers=head)
print(response.json())
assert response.status_code == 200