#!/usr/bin/env python
# 主函数使用方法
import pytest
def test_a():
    print('----begin test a')

def test_b():
    print('----begin test b')

if __name__ == '__main__':
    pytest.main("-s pytestdemo.py")