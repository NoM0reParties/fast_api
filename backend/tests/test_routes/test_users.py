import json


def test_create_user(client):
    data = {"username": "test_username", "email": "abc@test.com", "password": "121fws"}
    response = client.post("/users/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "abc@test.com"
    assert response.json()["is_active"] == True
