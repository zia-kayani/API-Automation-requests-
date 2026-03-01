import os
import requests
from requests.auth import HTTPDigestAuth

# ----------- basic auth --------------
def test_basicAuthentication():
    res = requests.get(url="https://postman-echo.com/basic-auth", auth=("postman", "password"))
    assert res.status_code == 200, "status code is not 200"
    data = res.json()
    print(data)
    assert data["authenticated"] == True, "Authentication failed"

# ----------- digest auth --------------
def test_digestAuthuntication():
    res = requests.get(url="https://postman-echo.com/digest-auth", auth=HTTPDigestAuth("postman", "password"))
    assert res.status_code == 200, "status code is not 200"
    data = res.json()
    print(data)
    assert data.get("authenticated" ) is True, "Authentication failed"


# ----------- Bear token auth -------
def test_bearerTokenAuthuntication():
    bearer_token = "i am not posting token hhhhhhh"
    headers =  {"Authorization": f"Bearer {bearer_token}"}
    res = requests.get(url="https://api.github.com/user", headers=headers)
    assert res.status_code == 200, "status code is not 200"
    print(res.json())


# -------------- API Key --------
def test_apiKeyAuthuntication():
    params = {
        "q": "London",
        "appid": "98a43e12d1f6ec257bc0e25d4e42cb97",
    }
    res = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=params)
    assert res.status_code == 200, f"expected 200, got {res.status_code}: {res.text}"
    print(res.json())


    