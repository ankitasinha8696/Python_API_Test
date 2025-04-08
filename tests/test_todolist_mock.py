import requests, pytest, requests_mock
from conftest import BASE_URL_TODOLIST

def test_create_new_item_mock():

    payload = {
                    "id": "0001",
                    "item": "API Testing"
              }
    
    with requests_mock.Mocker() as mock:
        mock.post(BASE_URL_TODOLIST, json = payload)
        response = requests.post(BASE_URL_TODOLIST, json = payload)

        assert response.status_code == 200, f"Item creation failed"

        print(response.json())

def test_delete_item():

    delete_id = "0005"

    delete_endpoint = f"{BASE_URL_TODOLIST}/{delete_id}"

    with requests_mock.Mocker() as mock:
        mock.delete(delete_endpoint)
        response = requests.delete(delete_endpoint)

        assert response.status_code == 200, f"Deletion failed"

        print(response)