list=["小明","小红","小兰"]
import random
while True:     #死循环
    print("1.随机点名    2.随机处罚")
    id=input("请输入编号：")
    #判断是不是id是不是数字，若是，则转换成int，否则反之
    if id.isdigit():#检查是否是阿拉伯数字
        id=int(id)
        if id==1:
            rannum=random.randint(0,len(list)-1)#随机获取一个编号
            print(list[rannum])#随机打印一个姓名
        elif id == 2:
             a=random.randint(0,100)
             print("恭喜您已被处罚",a,"遍！")
    elif id == "q" or id=="Q":
        print("欢迎下次光临！！")
        break
    else:
        print("对不起，输入非法")















