import unittest
from HTMLTestRunner import HTMLTestRunner
#1.创建测试集
suite = unittest.TestSuite()

#2.让测试加载器自己加载测试数据
tests = unittest.defaultTestLoader.discover(r"E:\Program Files (x86)\pythonProject\day16\tset_bank",pattern="Test*.py")

#3.将所有用例 放入测试集
suite.addTests(tests)

#4.创建测试运行器
f = open(file="中国工商银行测试报告.HTML",mode="w+",encoding="UTF-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream = f,
    title = "中国工商银行测试报告！",
    verbosity = 2,
    description = "执行了开户、存钱、取钱、转账、查询用例"
)

#5.让运行器生成测试报告
runner.run(suite)






