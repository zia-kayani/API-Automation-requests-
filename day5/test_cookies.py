import requests

class TestCookies:
    BASE_URL = "http://www.google.com"

    def test_set_cookie(self):
        response = requests.get(f"{self.BASE_URL}")
        assert response.status_code == 200, "wrong status code"
        #print all cookies
        all_cookies = response.cookies
        print(all_cookies)

        #assert cookies and check is not none
        assert all_cookies["AEC"], "AEC cookie is missing"
        assert all_cookies.get("AEC") is not None, "AEC cookie value is None"

        #extract specific cookie value
        Aec_cookie = all_cookies["AEC"]
        print("AEC cookie value:", Aec_cookie)

        #iterate through each cookie and print name and value
        for key, value in all_cookies.items():
            print(f"Cookie Name: {key}, Cookie Value: {value}") 

    