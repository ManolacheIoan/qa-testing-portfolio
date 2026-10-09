import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture
def session():
    """Reusable HTTP session, closed after each test."""
    s = requests.Session()
    yield s
    s.close()


@pytest.mark.parametrize("user_id", [1, 2, 3, 10])
def test_existing_users_return_200(session, user_id):
    response = session.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id


@pytest.mark.parametrize("user_id", [0, 11, 9999])
def test_nonexistent_users_return_404(session, user_id):
    response = session.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 404


@pytest.mark.parametrize(
    "title, body",
    [
        ("first post", "hello"),
        ("", "empty title"),
        ("long body", "x" * 1000),
    ],
)
def test_create_post_returns_201(session, title, body):
    payload = {"title": title, "body": body, "userId": 1}
    response = session.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == title
