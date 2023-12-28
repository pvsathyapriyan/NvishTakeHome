# from fastapi.testclient import TestClient
# client = TestClient(app)
import requests


host = "http://localhost/nvish"
token = "ABC"


def test_read_employee():
    headers = {"Authorization": token}
    response = requests.get(f"{host}/get/1", headers=headers)
    assert response.status_code == 200


def test_read_employee_not_found():
    headers = {"Authorization": token}
    response = requests.get(f"{host}/get/999", headers=headers)
    assert response.status_code == 404


def test_create_employee():
    payload = {"name": "Sathya"}
    headers = {"Authorization": token}
    response = requests.post(f"{host}/save", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == "Sathya"


def test_delete_employee():
    # Assuming there's an employee with empid=2 in the database
    headers = {"Authorization": token}
    response = requests.delete(f"{host}/delete/2", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"empid": 2, "message": "deleted"}


def test_read_employee_unauthenticated():
    headers = {"Authorization": "invalid_token"}
    response = requests.get(f"{host}/get/1", headers=headers)
    assert response.status_code == 400


def test_create_employee_unauthenticated():
    payload = {"name": "NewEmployee"}
    headers = {"Authorization": "invalid_token"}
    response = requests.post(f"{host}/save", json=payload, headers=headers)
    assert response.status_code == 400


def test_delete_employee_unauthenticated():
    # Assuming there's an employee with empid=2 in the database
    headers = {"Authorization": "invalid_token"}
    response = requests.delete(f"{host}/delete/2", headers=headers)
    assert response.status_code == 400

