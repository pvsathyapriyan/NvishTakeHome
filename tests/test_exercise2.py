# from fastapi.testclient import TestClient
# client = TestClient(app)
import requests


host = "http://localhost/nvish"
token = "ABC"


def test_authorize_success():
    headers = {"Authorization": token}
    response = requests.get(f"{host}/authorize", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"isAuthenticated": True, "message": "success"}


def test_authorize_failure():
    headers = {"Authorization": "invalid_token"}
    response = requests.get(f"{host}/authorize", headers=headers)
    assert response.status_code == 400
    assert response.json() == {"isAuthenticated": False, "message": "authentication failed"}
