import json


def test_create_job(client):
    data = {"title": "test_title", "company": "test inc", "company_url": "https://www.company.com",
            "location": "RUSSIA", "description": "testing", "date_posted": "2021-08-29"}
    response = client.post("/job/create-job", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["company"] == "test inc"
    assert response.json()["company_url"] == "https://www.company.com"


def test_retrieve_job_by_id(client):
    data = {"title": "test_title", "company": "test inc", "company_url": "https://www.company.com",
            "location": "RUSSIA", "description": "testing", "date_posted": "2021-08-29"}
    response = client.post("/job/create-job", json.dumps(data))
    response = client.get("/job/get/1")
    assert response.status_code == 200
    assert response.json()["title"] == "test_title"
