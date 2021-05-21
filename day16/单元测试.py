import unittest
from Calc import Calc
class TestCalc(unittest.TestCase):

    def test_Add1(self):
        #1.准备测试数据
        x = 5
        y = 8
        s = 13 #期望结果

        #调用测试方法
        calc = Calc()
        sum = calc.add(x,y)

        #断言
        self.assertEqual(s,sum)