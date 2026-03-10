import pytest 
import requests
import json
from faker import Faker

BASE_URL = "https://gorest.co.in/public/v2/users"
TOKEN = "01292e7bd3d14f602ab240c387af7a7929761cee332974bf471176bd9aa526bd"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# @pytest.fixture(scope="session", autouse=True)
def create_user():
    faker = Faker()
    data = {
        "name": faker.name(),
        "gender": "Male",
        "email": faker.unique.email(),
        "status": "inactive"
    }
    response = requests.post(BASE_URL, json=data, headers=HEADERS)
    assert response.status_code == 201, "Create user failed"
    print("\nCREATE Response:\n", json.dumps(response.json(), indent=4))
    return response.json()["id"]