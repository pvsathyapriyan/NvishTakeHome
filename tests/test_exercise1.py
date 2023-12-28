# from fastapi.testclient import TestClient
# client = TestClient(app)
import requests


host = "http://localhost/nvish"


def test_ping():
    response = requests.get(f"{host}/ping")
    assert response.status_code == 200
    assert response.json() == {"isSuccess": True}
