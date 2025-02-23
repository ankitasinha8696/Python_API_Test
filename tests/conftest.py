import pytest
import requests
import random

global BASE_URL
BASE_URL = "https://magento.softwaretestingboard.com/rest/V1"

@pytest.fixture
def generate_unique_email():
    """Generates a unique email to prevent duplicate registration issues."""
    return f"testuser{random.randint(1000, 9999)}@example.com"