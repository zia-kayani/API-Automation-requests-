import requests
import json
import pytest
from dataclasses import dataclass

BASE_URL = "http://localhost:3000/students"
USER_ID = None
HEADERS = {"Content-type": "application/json"}

#Post request payload with json module -------------------------------------------
def test_createStudentUsingDictionary():
    global USER_ID
    REQUEST_BODY = {
                "name":"Ali basit",
                "location":"DHA",
                "phone": "000000000",
                "courses" : [
                    "React Native",
                    "Flutter"
                ]
    }   

    # res = requests.post(url=BASE_URL, json=REQUEST_BODY)
    res = requests.post(url=BASE_URL ,  data=json.dumps(REQUEST_BODY), headers=HEADERS)

    assert res.status_code == 201, "status code is not 201"
    data  = res.json()
    assert data["name"] == "Ali basit", "incorrect name"
    assert data["location"] =="DHA", "Location is incorrect"
    assert data["phone"] == "000000000"
    assert data["courses"][0] == "React Native"
    assert data["courses"][1] == "Flutter"
    USER_ID =  data["id"]


#Post request payload with custom python class -------------------------------------------
def test_createStudentUsingCustomClass():
    global USER_ID 

    class Student():
        def __init__(self, name, location, phone, courses):
            self.name = name
            self.location = location
            self.phone = phone
            self.courses =  courses

    student = Student( name = "Saba" , location= "Janwai", phone= "123213", courses= [".Net", "Anguler"])
    REQUEST_BODY = student.__dict__

    # res = requests.post(url=BASE_URL, json=REQUEST_BODY)
    res = requests.post(url=BASE_URL ,  data=json.dumps(REQUEST_BODY), headers=HEADERS)

    assert res.status_code == 201, "status code is not 201"
    data  = res.json()
    assert data["name"] == "Saba", "incorrect name"
    assert data["location"] =="Janwai", "Location is incorrect"
    assert data["phone"] == "123213"
    assert data["courses"][0] == ".Net"
    assert data["courses"][1] == "Anguler"
    USER_ID =  data["id"]


#Post request payload with data class class -------------------------------------------
def test_createStudentUsingDataClass():
    global USER_ID 

    @dataclass
    class Student():
        name: str
        location: str
        phone: str
        courses : list

    student = Student( name = "Saba" , location= "Janwai", phone= "123213", courses= [".Net", "Anguler"])
    REQUEST_BODY = student.__dict__

    # res = requests.post(url=BASE_URL, json=REQUEST_BODY)
    res = requests.post(url=BASE_URL ,  data=json.dumps(REQUEST_BODY), headers=HEADERS)

    assert res.status_code == 201, "status code is not 201"
    data  = res.json()
    assert data["name"] == "Saba", "incorrect name"
    assert data["location"] =="Janwai", "Location is incorrect"
    assert data["phone"] == "123213"
    assert data["courses"][0] == ".Net"
    assert data["courses"][1] == "Anguler"
    USER_ID =  data["id"]

#Post request payload with data class class -------------------------------------------
def test_createStudentUsingExternalFile():
    global USER_ID 
    global REQUEST_BODY

    with open("./body.json" , "r")  as file:
     REQUEST_BODY = json.load(file)

    # res = requests.post(url=BASE_URL, json=REQUEST_BODY)
    res = requests.post(url=BASE_URL ,  data=json.dumps(REQUEST_BODY), headers=HEADERS)

    assert res.status_code == 201, "status code is not 201"
    data  = res.json()
    assert data["name"] == "Saba", "incorrect name"
    assert data["location"] =="Janwai", "Location is incorrect"
    assert data["phone"] == "123213"
    assert data["courses"][0] == ".Net"
    assert data["courses"][1] == "Anguler"
    USER_ID =  data["id"]



@pytest.fixture(autouse=True)
def teardown():
    yield
    response =  requests.delete(f"{BASE_URL}/{USER_ID}")
    assert response.status_code == 200, "Status code is not 200"
    print(response.json())
    print("user deleted successfully")



