import requests
from conftest import BASE_URL_GOREST

def test_fetch_all_user_data():

    endpoint = f"{BASE_URL_GOREST}/users"

    response = requests.get(endpoint)

    assert response.status_code == 200, "User data not fetched"

    for entry in response.json():
        for key, value in entry.items():
            print(f"{key}: {value}")

def test_fetch_specific_user_data():

    endpoint = f"{BASE_URL_GOREST}/users/7727046"

    response = requests.get(endpoint)

    assert response.status_code == 200, "User data not fetched"

    for key, value in response.json().items():
        print(f"{key}: {value}")

def test_fetch_specific_posts():
    endpoint = f"{BASE_URL_GOREST}/posts/195882"

    response = requests.get(endpoint)

    assert response.status_code == 200, "User posts not fetched"

    for key, value in response.json().items():
        print(f"{key}: {value}")

def test_fetch_all_posts():

    endpoint = f"{BASE_URL_GOREST}/posts"

    response = requests.get(endpoint)

    assert response.status_code == 200, "User posts not fetched"

    for entry in response.json():
        for key, value in entry.items():
            print(f"{key}: {value}")

def test_fetch_specific_user_posts():

    endpoint = f"{BASE_URL_GOREST}/users/7727563/posts"

    response = requests.get(endpoint)

    assert response.status_code == 200, "User posts not fetched"

    for entry in response.json():
        for key, value in entry.items():
            print(f"{key}: {value}")

def test_create_user():

    endpoint = f"{BASE_URL_GOREST}/users"

    headers = {
                "Authorization": f"Bearer 7eeb3813116deb094c3f85f98c15dbee232368c7be4505b8453ff87bfc7b1ae7",
                "Content-Type": "application/json"
              }

    payload = {
                "name":"Anahita Sharma",
                "email":"sharma_anahita@mosciski.example",
                "gender":"female",
                "status":"active"
              }
    
    response = requests.post(endpoint, json = payload, headers = headers)

    assert response.status_code == 201, "User did not get created"

    for key, value in response.json().items():
        print(f"{key}: {value}")

def test_create_post():

    endpoint = f"{BASE_URL_GOREST}/users/7727563/posts"

    headers = {
                "Authorization": f"Bearer 7eeb3813116deb094c3f85f98c15dbee232368c7be4505b8453ff87bfc7b1ae7",
                "Content-Type": "application/json"
              }
    
    payload =  {
                "title": "First Post",
                "body": "Hello GoRest."
               }
    
    response = requests.post(endpoint, json = payload, headers = headers)

    assert response.status_code == 201, f"Failure to create new post"