#!/usr/bin/env python

"""
在pytest框架中，有如下约束：
.兼容unittest与nose
.所有的单测文件名都需要满足test_*.py格式或*_test.py格式。
.在单测文件中，可以包含test_开头的函数，也可以包含Test开头的类。
.在单测类中，可以包含一个或多个test_开头的函数。
"""
# 主函数使用方法
import pytest
def test_a():
    print('----begin test a')
    assert 1

def test_b():
    print('----begin test b')
    assert 2

if __name__ == '__main__':
    pytest.main("-s pytestdemo.py")

