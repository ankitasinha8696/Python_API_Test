import pytest
import requests
import random

global BASE_URL, login_endpoint
BASE_URL_MAGENTO = "https://magento.softwaretestingboard.com/rest/V1"
BASE_URL_GOREST = "https://gorest.co.in/public/v2"
BASE_URL_TODOLIST = "http://localhost:8080/todolist"
cust_login_endpoint = f"{BASE_URL_MAGENTO}/integration/customer/token"
admin_login_endpoint = f"{BASE_URL_MAGENTO}/integration/admin/token"

@pytest.fixture
def generate_unique_email():
    """Generates a unique email to prevent duplicate registration issues."""
    return f"testuser{random.randint(1000, 9999)}@example.com"

@pytest.fixture
def get_customer_token():
    #Get customer token for admin specific operations
    payload = {
                "username": "ankitasinha322@gmail.com",
                "password": "Password1"
              }

    response = requests.post(cust_login_endpoint, json = payload)

    #Assertion
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    token = response.text.strip()
    return token

def get_admin_token():
    #Get admin token for admin specific operations
    payload = {
                "username": "ankitasinha322@gmail.com",
                "password": "Password1"
              }

    response = requests.post(admin_login_endpoint, json = payload)

    #Assertion
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    token = response.text.strip()
    return token