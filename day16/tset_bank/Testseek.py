import unittest
from day16.util.User import User
from day16.util.Bank import Bank

class TestSeek(unittest.TestCase):
    user = None
    bank = None
    def setUp(self) -> None:
        self.user = User()
        self.bank = Bank()

    def test_seek1(self):
        self.user.setAccount("qqq666")
        self.user.setPassword("123456")
        #预期结果
        teststart = 0

        start = self.bank.bank_seek(self.user.getAccount(),self.user.getPassword())

        self.assertEqual(teststart,start)

    def test_seek2(self):
        self.user.setAccount("qqqqqq15")
        self.user.setPassword("123456")

        teststart = 1

        start = self.bank.bank_seek(self.user.getAccount(),self.user.getPassword())

        self.assertEqual(teststart,start)
    #
    # def test_seek3(self):
    #     self.user.setAccount("qqqqqq16")
    #     self.user.setPassword("weqweqw")
    #
    #     teststart = 2
    #
    #     start = self.bank.bank_seek(self.user.getAccount(),self.user.getPassword())
    #
    #     self.assertEqual(teststart,start)