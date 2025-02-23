import pytest
import requests
import random
from conftest import BASE_URL

endpoint = f"{BASE_URL}/integration/customer/token"

def test_user_login():
    payload = {
                "username": "ankitasinha322@gmail.com",
                "password": "Password1"
              }

    response = requests.post(endpoint, json = payload)

    #Assertion
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    token = response.text.strip()
    print(token)

def test_user_login_invalid():
    payload = {
                "username": "ankitasinha323@gmail.com",
                "password": "Password1"
              }

    response = requests.post(endpoint, json = payload)

    #Assertion
    assert response.status_code == 401, f"Expected 401 failure, got {response.status_code}"
    print(response.status_code)
    assert "message" in response.text, f"Did not get the expected error message"
