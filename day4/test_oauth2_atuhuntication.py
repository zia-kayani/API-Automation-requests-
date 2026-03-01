import requests
import pytest

access_token = None

@pytest.fixture(scope="session", autouse=True)
def generate_toeken():
    global access_token
    client_id = "42ca6b0f61d64905bd0a63952c8270a3"
    client_secret = "78060629a5fc4234a05aee9acea90f28"
    token_url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    form_data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    res =  requests.post(url=token_url, headers=headers, data=form_data)
    assert res.status_code == 200, f"expected 200, got {res.status_code}"
    print(res.json())
    access_token =  res.json()["access_token"]

#-------------oauth 2 authuntication -------------
class TestOAuth2Authuntication:
    def test_get_arijit_singh_top_tracks(self):
        assert access_token is not None, "Access token was not generated"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }   
        res = requests.get(url="https://api.spotify.com/v1/artists/4YRxDV8wJFPHPTeXepOstw/top-tracks?market=IN",
                            headers=headers, params={"market": "IN"})
        assert res.status_code == 200, f"expected 200, got {res.status_code}"
        print(res.json())        




