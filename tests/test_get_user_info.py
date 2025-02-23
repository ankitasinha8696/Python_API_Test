import pytest
import requests
import random
from conftest import BASE_URL

login_endpoint = f"{BASE_URL}/integration/customer/token"
userdata_endpoint = f"{BASE_URL}/customers/me"

def test_get_user_info_valid():
    payload = {
                "username": "ankitasinha322@gmail.com",
                "password": "Password1"
              }

    response = requests.post(login_endpoint, json = payload)

    #Assertion
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    jwt_token = response.text.strip()

    headers = {
                "Authorization": f"Bearer: {jwt_token}",
                "Content-Type": "application/json"
             }
    
    user_info = requests.get(userdata_endpoint, headers = headers)

    user_info.status_code == 200, f"Failed to fetch user details"
    print(user_info.json()["message"])

def test_get_user_info_invalid():
    payload = {
                "username": "ankitasinha323@gmail.com",
                "password": "Password123"
              }

    response = requests.post(login_endpoint, json = payload)

    #Assertion
    assert response.status_code == 401, f"Expected 200, got {response.status_code}"
    print(response.json()["message"])