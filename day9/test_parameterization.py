import pytest


class TestParameterization:
    @pytest.mark.parametrize("num1, num2", [(1,1), (2,2), (2,3  ),(5,10)])
    def test_caculation(self, num1, num2):
        assert num1 == num2
