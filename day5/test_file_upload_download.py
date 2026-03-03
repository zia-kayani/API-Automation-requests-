import requests
import os

class TestFileUploadDownload:
    BASE_URL = "http://localhost:8080"
    file1 = os.path.join(os.path.dirname(__file__), "Testfile1.txt")
    file2 = os.path.join(os.path.dirname(__file__), "Testfile2.txt")

    #single file upload
    def test_file_upload(self):

        with open(self.file1, "rb") as file:
            files = {"file": file}

            response = requests.post(f"{self.BASE_URL}/uploadFile", files=files)
            assert response.status_code == 200, "wrong status code"
            data = response.json()
            assert data["fileName"] == "Testfile1.txt", "wrong filename"
            print(data)

    #multiple file upload
    def test_multiple_file_upload(self):
        with open(self.file1, "rb") as file1, open(self.file2, "rb") as file2:
            files = {("files", file1), ("files", file2)}

            response = requests.post(f"{self.BASE_URL}/uploadMultipleFiles", files=files)
        assert response.status_code == 200, "wrong status code"
        data = response.json()
        print(data)
        
    #file download
    def test_file_download(self):
        fileName = "Testfile1.txt"
        response = requests.get(f"{self.BASE_URL}/downloadFile/{fileName}")
        assert response.status_code == 200, "wrong status code"
        output_path = f"downloaded_{fileName} "
        with open(output_path, "wb") as file:
            file.write(response.content)