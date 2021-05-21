import unittest
from Calc import Calc
from ddt import ddt
from ddt import data
from ddt import unpack
#数据源，造三组数据
da = [
    [1,2,3],
    [3,5,8],
    [-7,-9,-16],
    [-4,5,1],
    [-8,6,-2]
]

@ddt   #1.将测试类用@ddt修饰
class CalcTest(unittest.TestCase):
    @data(*da)  #引入数据源
    @unpack     #将数据源的数据进行解包,不然的话会当成一个整体传进来
    def test_Add(self,a,b,c):#a,b,c就是每组数据的3个元素，c是期望结果
        calc = Calc()
        sum = calc.add(a,b)
        self.assertEqual(c,sum)