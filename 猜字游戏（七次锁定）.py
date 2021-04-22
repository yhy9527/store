
import random
#让系统产生一个随机数
num=random.randint(1,101)

#金币
coin = 100
#次数统计
count = 0
while True:  #死循环

    if count < 7:
        count = count + 1
        num1=input("请输入一个随机数：")
        num1=int(num1)#强制转换类型
        if num1 > num :
            print("大了")
        elif num1 < num :
            print("小了")
        else:
            print("恭喜你，中奖了！中奖号码：",num,"您本次猜了",count,"次")
            break  #中断，直接跳出循环
    else:
        print("系统已退出")
        break