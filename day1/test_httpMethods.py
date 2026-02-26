import requests
import pytest

global user_id

HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": "reqres_577ec103946c48efbc3120cc18e7e938"
}

#get request
@pytest.mark.order(1)
def test_get_users():
    res = requests.get(
        url="https://reqres.in/api/users?page=2",
        headers=HEADERS
    )

    assert res.status_code == 200, "Wrong status"
    assert res.headers["Content-Type"] == "application/json; charset=utf-8", "Wrong content type"
    assert res.elapsed.total_seconds() < 2, "Too slow"

    data = res.json()

    assert data.get("data") is not None, "Data missing"
    print(data)

    assert data.get("page") == 2, "Wrong page"
    assert "email" in res.text, "Email not found"

#post request 
@pytest.mark.order(2)
def test_add_user():
    global user_id
    PAYLOAD = { "name":"zia", "job":"trainer"}
    res = requests.post(url="https://reqres.in/api/users", json=PAYLOAD, headers=HEADERS)

    assert res.status_code == 201, "Wrong status"
    assert res.headers["Content-Type"] == "application/json; charset=utf-8", "Wrong content type"
    assert res.elapsed.total_seconds() < 2, "Too slow"

    data = res.json()

    assert data.get("name") == "zia", "Name mismatch"
    assert data.get("job") == "trainer", "Job mismatch"
    assert id in data, "id is missing "

    user_id= data["id"]



#update request
@pytest.mark.order(3)
def test_update_user():
    PAYLOAD = { "name":"Ali", "job":"teacher"}
    res = requests.put(url="https://reqres.in/api/users/{user_id}", json=PAYLOAD, headers=HEADERS)
    assert res.status_code == "200", "Wrong status code "
    assert res.headers["content-type"] == "application/json; charset=utf-8", "Wrong content type"
    assert res.elapsed.total_seconds() <2, "too slow"

    data = res.json()

    assert data.get("name" ) =="Ali" , "wrong name "
    assert data.get("job") ==  "teacher", "wrong job "
    assert "updated at"  in data, "Missing update info"
    print(data)


@pytest.mark.order(4)
def test_delete_user():
    res = requests.delete(url="https://reqres.in/api/users/{user_id}", headers=HEADERS)
    assert res.status_codes == "204" , "wrong status code "
    assert res.elapsed.total_seconds() < 2, "too slow response"
    assert res.text == "", "response is not empty "
    print("user delelted successfully ")
