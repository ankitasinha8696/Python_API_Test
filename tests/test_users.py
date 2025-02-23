import pytest
import requests
import random
from conftest import BASE_URL

pytest.mark.usefixtures("generate_unique_email")
def test_user_registration(generate_unique_email):
    """Test case for registering a new user."""
    endpoint = f"{BASE_URL}/customers"
    payload = {
        "customer": {
            "firstname": "Test",
            "lastname": "User",
            "email": generate_unique_email,
            "addresses": [],
        },
        "password": "Test@12345"
    }

    response = requests.post(endpoint, json=payload)
    
    # Assertions
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    response_data = response.json()
    print(response.status_code)
    for key, value in response_data.items():
        print(f"{key}: {value}")
    assert "id" in response_data, "User ID is missing in the response"
    assert response_data["email"] == generate_unique_email, "Email mismatch in response"


def test_duplicate_user_registration():
    """Test case for registering an already existing user."""
    endpoint = f"{BASE_URL}/customers"
    existing_email = "testuser@example.com"  # Replace with an actual registered email

    payload = {
        "customer": {
            "firstname": "Test",
            "lastname": "User",
            "email": existing_email,
            "addresses": [],
        },
        "password": "Test@12345"
    }

    response = requests.post(endpoint, json=payload)

    # Assertions
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    response_data = response.json()
    print(response.status_code)
    print(response_data["message"])
    assert "message" in response_data, "Error message not found in response"
    assert "already exists" in response_data["message"], "Expected error message for duplicate user"