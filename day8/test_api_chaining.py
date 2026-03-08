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

faker = Faker()
@pytest.mark.dependency(name="create")
class TestChainingAPIs:
    user_id = None  # class variable
    #Create User
    def test_create_user(self):
        data = {
            "name": faker.name(),
            "gender": "Male",
            "email": faker.unique.email(),
            "status": "inactive"
        }

        res = requests.post(BASE_URL, json=data, headers=HEADERS)
        assert res.status_code == 201, "wrong status code"

        TestChainingAPIs.user_id = res.json()["id"]
        assert TestChainingAPIs.user_id, "USER_ID is not generated"

        print("\nCREATE Resposne\n", json.dumps(res.json(), indent=4))

    #Get User
    @pytest.mark.dependency(depends=["create"])
    def test_get_user_details(self):
        res = requests.get(url=f"{BASE_URL}/{TestChainingAPIs.user_id}", headers=HEADERS)
        assert res.status_code == 200, "Get user failed"
        print("\nGET Response:\n", json.dumps(res.json(), indent=4))
    
    #Update user
    @pytest.mark.dependency(depends=["create"])
    def test_update_user(self):
        updated_data = {
            "name": faker.name(),
            "gender": "Male",
            "email": faker.unique.email(),
            "status": "active"
        }

        res = requests.put(url=f"{BASE_URL}/{TestChainingAPIs.user_id}", json=updated_data, headers=HEADERS)
        assert res.status_code == 200, "wrong status code"
        print("\nUPDATE Resposne\n", json.dumps(res.json(), indent=4))

    #Delete user
    @pytest.mark.dependency(depends=["create"])
    def test_delete_user(self):
        res = requests.delete(url=f"{BASE_URL}/{TestChainingAPIs.user_id}", headers=HEADERS)
        assert res.status_code == 204, "wrong status code"
