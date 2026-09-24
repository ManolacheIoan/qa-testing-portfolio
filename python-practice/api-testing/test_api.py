import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user_returns_200():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200

def test_get_user_has_correct_name():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.json()["name"] == "Leanne Graham"

def test_get_nonexistent_user_returns_404():
    response = requests.get(f"{BASE_URL}/users/99999")
    assert response.status_code == 404

def test_create_user():
    payload = {"name": "Ioan Manolache", "email": "ioan@test.com"}
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Ioan Manolache"

def test_create_user_response_has_id():
    payload = {"name": "Test User"}
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert "id" in response.json()