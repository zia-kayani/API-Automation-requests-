
class TestClass:
    def testMethod1(self):
        print("test method 1")
    def testMethod2(self):
        print("test method2")




import pytest

@pytest.mark.dependency()
@pytest.mark.order(1)
def test_open_app():
    print("opened app")
   # assert Fail

@pytest.mark.dependency(depends=['test_login'])
@pytest.mark.order(3)
def test_dashboard():
    print("opened dashboard")

@pytest.mark.dependency(depends=['test_open_app'])
@pytest.mark.order(2)
def test_login():
    print("login success")