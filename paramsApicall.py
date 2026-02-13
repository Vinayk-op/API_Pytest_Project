import requests

para = {
    "page": 2,
    "per_page": 3
}

url = "https://gorest.co.in/public/v2/users"

response = requests.get(url, params=para)
print(response.json())