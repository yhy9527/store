'''
    商城：
        1.商品
        2.薪资
        3.我的购物车
    逻辑：
        1.初始化您的薪资
        2.展示商城商品
        3.输入商品编号
        4.看钱够不够
            4.1够了，就添加我的购物车，薪资减去相对应的金额
            4.2不够，买其他的。
        继续买东西，一直到输入Q获取q，退出
        给商城添加以下功能：
1.	进入商城时候，随机抽奖某个商品的优惠券。
优惠券如下：
		10张辣条优惠券：满600减300
		20张Lenovo电脑优惠券：半折甩卖
2.	结算时，添加购物积分功能
10元1个积分。

'''
#商品  0  1  2  3  4  5  6
print("欢迎您进入商城！请您开始抽奖！")
import random
list = ["辣条优惠券","电脑优惠券"]
yhq=random.choice(list)
print("您获得的优惠券是：",yhq)
commodity = [
    ["电脑",6000],
    ["辣条",700],
    ["ipad",3000],
    ["qq糖",20],
    ["旺仔牛奶",100],
    ["iphone12",5000],
    ["水杯",100]
]
#初始化余额
purse=input("请输入您的余额：")
purse=int(purse)
purse1=purse

#购物车
mycart=[]

#展示商品
while True:
    for index,values in enumerate(commodity):#enumerate()枚举：将所有的可能都列举出来
        print(index,"    ",values)
    #输入要买商品的编号
    num=input("请输入要买商品的编号：")
    #商品编号 0 1 2 3 4 5 6    Q或q退出系统
    if num.isdigit():#判断是否是数字
        num=int(num)
        if num < len(commodity):#判断是否有这个商品
            if purse >= commodity[num][1]:
                if num == 0:
                    commodity[num][1] = commodity[0][1] / 2
                    print("感谢您使用电脑半折优惠券！")
                elif num == 1 and commodity[1][1] >=600:
                    commodity[num][1] = commodity[1][1] - 300
                    print("感谢使用辣条满600减300优惠券！")
                mycart.append(commodity[num])#添加到购物车
                purse = purse - commodity[num][1]#计算余额
                print("商品已加入购物车。钱包余额：",purse,)
            else:
                print("您的余额不足！")
        else:
            print("商品编号不存在！！请重新输入")
    elif num =="Q" or num=="q":
        print("---------欢迎您下次光临！！！-----------")
        break
    else:
        print("输入非法！")
#打印购物小票
print("您本次购买的商品：")
for index,values in enumerate(mycart):
    print(index,"  ",values)
    jf =int((purse1-purse )/ 10)
print("您的余额：",purse,"积分：",jf)








