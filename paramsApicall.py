import requests


# For paged results parameter "page" and "per_page" should be passed in url
# ex: GET /public/v2/users?page=1&per_page=20 (max 100 results per page)
#
# Request methods PUT, POST, PATCH, DELETE needs access token, which needs
# to be passed with "Authorization" header as Bearer token.

para = {
    "page": 2,
    "per_page": 3
}

url = "https://gorest.co.in/public/v2/users"

response = requests.get(url, params=para)
print(response.json())