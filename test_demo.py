import pytest
import requests

url = "https://reqres.in"

head = {
    "accept": "application/json",
    "x-api-key": "reqres_c1a8f5ff75344b9e8d49ad77e0465a00"
}

def test_get_request():
    response = requests.get(url=str(url+"/api/users"), headers=head)
    assert response.status_code == 200
    print(response.text)
