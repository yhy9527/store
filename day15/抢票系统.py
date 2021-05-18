'''
    抢票：
        起始票数：500
        3个人：张三，李四，王五黄牛，同时抢票
        1.人要抢票，人要实现多线程。
        2.500张抢完为止
'''
from threading import Thread
import  time

tiket = 200000

class Person(Thread):
    username = ""
    count  = 0

    def run(self) -> None:
        global  tiket  # 将tiket 申明为全局变量，在方法里进行使用
        while True:
            if tiket <= 0:

                print("对不起，",self.username,"没有抢到票了！")
                print(self.username,"本次抢了",self.count,"张票！")
                break
            else:

                tiket = tiket - 1
                self.count = self.count + 1
                print("恭喜",self.username,"抢到 1 张票，还剩",tiket,"张票！")
                time.sleep(2)

p1 = Person()
p2 = Person()
p3 = Person()

p1.username = "张家辉"
p2.username = "杜旱情"
p3.username = "旺财"


p1.start()
p2.start()
p3.start()

















