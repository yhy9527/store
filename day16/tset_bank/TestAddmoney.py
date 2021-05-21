import unittest
from day16.util.User import User
from day16.util.Address import Address
from day16.util.Bank import Bank

class TestAddMoney(unittest.TestCase):
    user = None
    address = None
    bank = None

    def setUp(self) -> None:
        self.user = User()
        self.bank = Bank()
        self.address = Address()

    def test_addMoney1(self):
        # 1.准备测试数据
        self.user.setAccount("kkk666")
        self.bank.setMoney("666")

        # 2.预期结果
        teststart = 1

        # 3.调用被测方法
        start = self.bank.bank_addMoney(self.user.getAccount(),self.bank.getMoney())

        # 4.断言
        self.assertEqual(teststart,start)

    # def test_addMoney2(self):
    #     # 1.准备测试数据
    #     self.user.setAccount("qqqqqqq3")
    #     self.bank.setMoney("10000")
    #
    #     # 2.预期结果
    #     teststart = False
    #
    #     # 3.调用被测方法
    #     start = self.bank.bank_addMoney(self.user.getAccount(),self.bank.getMoney())
    #
    #     # 4.断言
    #     self.assertEqual(teststart,start)