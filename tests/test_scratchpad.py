import requests, pytest, requests_mock

def test_typicode():
    base_url = "https://jsonplaceholder.typicode.com/"
    endpoint = "posts/"
    post_id = 1

    url = base_url + endpoint + str(post_id)

    response = requests.get(url)

    assert response.status_code == 200, "Failed to fetch post data"

    assert "title" in response.json(), "Incorrect data fetched"

def test_typicode_mock():
    base_url = "https://jsonplaceholder.typicode.com/"
    endpoint = "users/"
    user_id = 1

    url = base_url + endpoint + str(user_id)

    payload = {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com"
    }

    with requests_mock.Mocker() as mock:
        mock.get(url, json = payload)

        response = requests.get(url)

        if response.status_code == 200:
            print(response.json())
        else:
            print("Data not received")