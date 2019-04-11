#!/usr/bin/env python
import pytest
import allure
@allure.story("哇咔咔")
@pytest.mark.parametrize("x,y",[(3+6,8),(1+2,3),(2+9,11)])
def test_add(x,y):
    assert x == y


#allure generate report/xml -o report/html



