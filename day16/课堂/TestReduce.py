import unittest
from Calc import Calc
class TestReduce(unittest.TestCase):
    calc = None

    def setUp(self) -> None:  # 在所有测试方法之前运行
        self.calc = Calc()



    def test_reduce1(self):
        # 1.准备测试数据
        a = 6
        b = 7
        s = -1  # 期望结果

        # 调用被测方法
        sum = self.calc.reduce(a, b)  # sum 是实际结果

        # 断言
        self.assertEqual(s, sum)

    def test_reduce2(self):
        # 1.准备测试数据
        a = -6
        b = -7
        s = 1  # 期望结果

        # 调用被测方法

        sum = self.calc.reduce(a, b)  # sum 是实际结果

        # 断言
        self.assertEqual(s, sum)
    def test_reduce3(self):
        # 1.准备测试数据
        a = 9
        b = -7
        s = 16  # 期望结果

        # 调用被测方法
        sum = self.calc.reduce(a, b)  # sum 是实际结果

        # 断言
        self.assertEqual(s, sum)
    def test_reduce4(self):
        # 1.准备测试数据
        a = -9
        b = 8
        s = -17  # 期望结果

        # 调用被测方法
        sum = self.calc.reduce(a, b)  # sum 是实际结果

        # 断言
        self.assertEqual(s, sum)








