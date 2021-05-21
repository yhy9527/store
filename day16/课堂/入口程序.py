'''
    使用测试集来进行测试：
'''
import unittest
from HTMLTestRunner  import  HTMLTestRunner
# 1.创建测试集
suite = unittest.TestSuite()
# 2.让测试加载器自己加载所用用例
tests = unittest.defaultTestLoader.discover(r"E:\Program Files (x86)\pythonProject\day16\课堂",pattern="Test*.py")
# 3.将所用例 放入测试集
suite.addTests(tests)
# 4.创建测试运行器
f = open(file="E:\Program Files (x86)\pythonProject\day16\课堂\计算器测试报告.html",mode="w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream = f,
    title="这是一个计算器测试报告！",
    verbosity=2,
    description="执行了加法和减法用例"
)
# 5.让运行器生成测试报告

runner.run(suite)










