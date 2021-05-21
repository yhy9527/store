'''
    测试方法：
        边界值、等价类、场景法、因果法、错误探测法
    1.边界值：
        int : 2^31 - 1  能表示的最大数据
    2.-9  + 9
        9 + 9
        -9 + -9
        9 + -8
    unittest单元测试框架：
    1. 测试类继承unittest.TestCase
    2. 测试类里写测试方法：必须testxxxxxx
'''
import unittest
from Calc import Calc
class  TestCalc(unittest.TestCase): # 类就是单元测试的子类

    def test_Add1(self):
        # 1.准备测试数据
        a = 6
        b = 7
        s = 13  # 期望结果

        # 调用被测方法
        calc = Calc()
        sum = calc.add(a,b) # sum 是实际结果

        # 断言
        self.assertEqual(s,sum)


    def test_Add2(self):
        # 1.准备测试数据
        a = -6
        b = -7
        s = -13  # 期望结果

        # 调用被测方法
        calc = Calc()
        sum = calc.add(a, b)  # sum 是实际结果

        # 断言
        self.assertEqual(s, sum)
    def test_Add3(self):
        # 1.准备测试数据
        a = -6
        b = 6
        s = 0  # 期望结果

        # 调用被测方法
        calc = Calc()
        sum = calc.add(a, b)  # sum 是实际结果

        # 断言
        self.assertEqual(s, sum)


    def test_Add4(self):
        # 1.准备测试数据
        a = -6
        b = 6999999999999999999999999999999999999999999999999999999999999
        s = 6999999999999999999999999999999999999999999999999999999999993  # 期望结果

        # 调用被测方法
        calc = Calc()
        sum = calc.add(a, b)  # sum 是实际结果

        # 断言
        self.assertEqual(s, sum)










