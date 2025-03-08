import requests
import pytest
from conftest import BASE_URL_TODOLIST

@pytest.mark.skip
def test_create_new_item():

    payload = {
                "id": "0005",
                "item": "API Testing"
              }
    
    response = requests.post(BASE_URL_TODOLIST, json = payload)

    assert response.status_code == 202, f"Item creation failed"

    print(response)

@pytest.mark.skip
def test_delete_item():

    delete_id = "0005"

    delete_endpoint = f"{BASE_URL_TODOLIST}/{delete_id}"

    response = requests.delete(delete_endpoint)

    assert response.status_code == 204, f"Deletion failed"

    print(response)

@pytest.mark.skip
def test_update_item():

    update_id = "0003"

    update_endpoint = f"{BASE_URL_TODOLIST}/{update_id}"

    payload = {
                "id": "0003",
                "item": "Brush up OOPs concepts"
              }

    response = requests.put(update_endpoint, json = payload)

    response.status_code == 202, f"Update failed"

def test_move_item():

    move_id = "0002"
    move_endpoint = f"{BASE_URL_TODOLIST}/{move_id}/move"

    payload = {
               "position": "before",
               "targetId": "0001"
              }
    
    response = requests.post(move_endpoint, json = payload)

    assert response.status_code == 204, f"Failed to move content"

def test_get_all_items():

    response = requests.get(BASE_URL_TODOLIST)

    response.status_code == 200, f"Items successfully fetched"

    print(response.json())