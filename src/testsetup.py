#!/usr/bin/env python
"""
pytest有哪些优点？
允许直接使用assert进行断言，而不需要使用self.assert*;
可以自动寻找单测文件、类和函数;
Modular fixtures可以用于管理小型或参数化的测试信息;
与unittest和nose单测框架兼容;
兼容性较好，支持Python 2.7，Python 3.4+。
丰富的插件支持，共计有超过315个插件支持;
"""
# Pytest的setup和teardown函数
#
# 1.setup和teardown主要分为：模块级,类级，功能级，函数级。
# 2.存在于测试类内部
# 代码示例：
#
# 函数级别setup()／teardown()
# 运行于测试方法的始末，即:运行一次测试函数会运行一次setup和teardown

import pytest
class Test_ABC:
    # 测试类级别的setup teardown  在类中只执行一次
    # # 测试类级开始
    # def setup_class(self):
    #     print("------->setup_class")
    #
    # # 测试类级结束
    # def teardown_class(self):
    #     print("------->teardown_class")

  # 函数级开始
  def setup(self):
      print("------->setup_method")
  # 函数级结束
  def teardown(self):
      print("------->teardown_method")
  def test_a(self):
      print("------->test_a")
      assert 1
  def test_b(self):
      print("------->test_b")
if __name__ == '__main__':
              pytest.main()




