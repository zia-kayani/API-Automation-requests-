import requests

class TestHeaders:
    def test_response_headers(self):
        response  = requests.get("http://www.google.com")
        assert response.status_code == 200, "wrong status code"
        all_headers = response.headers
        print(all_headers)

        #extract specific header
        print("date header:", all_headers["Date"])

        #Assertions
        assert all_headers["Content-Type"] == "text/html; charset=ISO-8859-1", "wrong content type"
        assert all_headers.get("content-encoding") == "gzip", "wrong content encoding"
        assert all_headers.get("server") == "gws", "wrong server"