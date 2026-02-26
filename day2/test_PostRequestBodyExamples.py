import requests
import json

BASE_URL = "http://localhost:3000/students"
USER_ID = None
HEADERS = {"Content-type": "application/json"}

#Post request with Dictionary 
def test_createStudentUsingDictionary():
    REQUEST_BODY = {
                "name":"shayan",
                "location":"Lahore",
                "phone": "039999999",
                "courses" : [
                    "React js",
                    "Anguler js"
                ]
    }   

    # res = requests.post(url=BASE_URL, json=REQUEST_BODY)
    res = requests.post(url=BASE_URL ,  data=json.dumps(REQUEST_BODY), headers=HEADERS)

    assert res.status_code == 201, "status code is not 201"
    data  = res.json()
    assert data["name"] == "shayan", "incorrect name"
    assert data["location"] =="Lahore", "Location is incorrect"
    assert data["phone"] == "039999999"
    assert data["courses"][0] == "React js"
    assert data["courses"][1] == "Anguler js"
    USER_ID =  data["id"]

