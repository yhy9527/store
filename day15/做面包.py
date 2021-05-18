import threading
import time

basket = 0
class Cooker(threading.Thread):
    username = ""
    def run(self) -> None:
        global basket
        while True:
            if basket <= 100 :
                basket += 1

                print( "厨师共做了", basket, "个面包！")
                time.sleep(3)
            else:
                print("篮子满了！！停几分钟！！")
                time.sleep(5)


num = 0
class Customer(threading.Thread):
    customer_name = " "
    def run(self) -> None:
        global basket
        global num
        global times
        if times < 301:
            if basket > 0:
                basket -= 1
                num += 1
                time.sleep(1)
                print(self.customer_name,"买了",num,"个面包！！！！花了",num*10,"元！！！")

        else:
            print("没面包了，等会！！！")



times = 0
class Time(threading.Thread):
    def run(self) -> None:
        global times
        while True:
            if times < 301:
                time.sleep(1)
                times += 1



t = Time()
p1 = Cooker()
p2 = Cooker()
p3 = Cooker()
p4 = Cooker()
p5 = Cooker()
p6 = Cooker()
c1 = Customer()
c2 = Customer()
c3 = Customer()
c4 = Customer()
c5 = Customer()
c6 = Customer()
#厨师
p1.username = "张家辉"
p2.username = "杜旱情"
p3.username = "旺财"
p4.username = "Q辉"
p5.username = "Q情"
p6.username = "Q财"
#顾客
c1.customer_name = "小明"
c2.customer_name = "小米"
c3.customer_name = "小红"
c4.customer_name = "小未"
c5.customer_name = "小英"
c6.customer_name = "小嗯"
#启动厨师
t.start()
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()
#启动顾客
c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()




































