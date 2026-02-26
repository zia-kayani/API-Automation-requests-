import pytest

@pytest.fixture()
def setup():
    print("browser launched")
    yield
    print("browser closed")

class TestClass:
    def test_Login(self, setup):
        print("test login function")
    def test_Search(self, setup):
        print("test search function")
