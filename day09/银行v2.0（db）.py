import random
from DBUtils import update
from DBUtils import select

# 导包、全局变量

# 1. 空的银行的库 ： 100个

# 2.银行的名称写死
bank_name = "中国工商银行的昌平支行"

# 打印欢迎页面
def welcome():
    print("---------------------------------")
    print("-     中国工商银行账户管理系统V1.0     -")
    print("---------------------------------")
    print("-   1.开户                       -")
    print("-   2.存钱                       -")
    print("-   3.取钱                       -")
    print("-   4.转账                       -")
    print("-   5.查询                       -")
    print("-   6.Bye!                       -")
    print("----------------------------------")

# 银行的开户逻辑
def bank_addUser(account,username,password,country,province,street,door):
    # 判断是否已满
    sql = "select count(*) from user_data"
    data = select(sql,[]) # ((72),(),())
    if data[0][0] >= 100:
        return 3
    # 判断是否存在
    sql1 = "select * from user_data where account = %s"
    data1 = select(sql1,account) #(("张三"),(“李四”))
    if len(data1) != 0:
        return 2
    #正常开户
    # 数据存到数据库里
    sql2 = "insert into user_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [account,username,password,country,province,street,door,0,bank_name]
    update(sql2,param2)
    return 1


# 用户开户方法
def addUser():
    # 随机获取账号
    li = ["1","2","3","4","5","6","7","8","9","0","a","b","c","e","f"]
    account = ""
    for i in range(8):
        index = random.randint(0, len(li) - 1)
        account = account + li[index]
    name = input("请输入用户名：")
    password = input("请输入您的密码（6位数字）：")
    print("接下来要输入您的地址信息：")
    country = input("\t输入国家：")
    province = input("\t输入省份：")
    street =  input("\t输入街道：")
    door = input("\t输入门牌号：")

    status = bank_addUser(account,name,password,country,province,street,door)
    if status == 1:
        print("恭喜开户成功！")
        info = '''
            ------------个人信息----------------
            账号：%s,
            用户名：%s,
            取款密码：%s,
            地址信息：
                国家：%s,
                省份：%s,
                街道：%s,
                门牌号：%s,
            余额：%s,
            开户行：%s
            -----------------------------------
        '''
        print(info % (account,name,password,country,province,street,door,0,bank_name))

    elif status == 2:
        print("对不起，该用户已存在！请稍后重试！！！")
    elif status == 3:
        print("对不起，该银行库已满，请携带证件到其他银行办理！！！")

#存钱
def deposite():
    account = input("请输入用户账号：")
    sql = "SELECT account FROM user_data where account = %s"
    param = [account]
    data = select(sql,param)
    if len(data) != 0:
        print("用户存在")
        je = int(input("请输入存钱金额："))
        sql1 = "UPDATE user_data set money = money +%s WHERE account = %s"
        param1 = [je,account]
        update(sql1,param1)
        print("存钱成功！！")
    else:
        return print("用户不存在！！")


#取钱
def withdraw_money():
    account = input("请输入用户账号：")
    sql = "SELECT account FROM user_data where account = %s"
    param = [account]
    data01 = select(sql, param)
    if len(data01) != 0:
        print("用户存在")
        password = input("请输入密码：")
        sql1 = "SELECT passwords FROM user_data where account = %s"
        param1 = [account]
        data02 = select(sql1,param1)
        if data02[0][0] == password:
            print("密码正确！")
            money = int(input("请输入取钱金额："))
            sql2 = "SELECT money FROM user_data where account = %s"
            param2 = [account]
            data03 = select(sql2,param2)
            if money <= data03[0][0]:
                sql2 = "UPDATE user_data set money = money -%s where account = %s"
                param3 = [money,account]
                update(sql2,param3)
                print("取钱成功！！")
            else:
                print("余额不足！！")
        else:
            print("密码错误！！")
    else:
        print("账户不存在！！")

#转账
def transfer_account():
    zc = input("请输入转出账号：")
    zr = input("请输入转入账号：")
    sql = "SELECT account FROM user_data where account = %s"
    param = [zc]
    data = select(sql, param)

    sql01 = "SELECT account FROM user_data where account = %s"
    param01 = [zr]
    data02 = select(sql01, param01)
    if len(data) != 0 and len(data02) != 0:
        print("用户存在")
        password = input("请输入转出密码：")
        sql02 = "SELECT passwords FROM user_data where account = %s"
        param02 = [zc]
        data02 = select(sql02, param02)
        if data02[0][0] == password:
            print("转出密码正确！")

            money = int(input("请输入转账金额："))
            sql03 = "SELECT money FROM user_data where account = %s"
            param03 = [zc]
            data03 = select(sql03, param03)
            if money <= data03[0][0]:

                sql04 = "UPDATE user_data set money = money -%s where account = %s"
                param04 = [money, zc]
                update(sql04, param04)
                sql05 = "UPDATE user_data set money = money +%s where account = %s"
                param05 = [money, zr]
                update(sql05, param05)
                print("转账成功！！")
            else:
                print("余额不足！！")
        else:
            print("转出密码错误！！")
    else:
        print("用户不存在！！")

#查询
def query():
    account = input("请输入账号：")
    sql01 = "SELECT * FROM user_data WHERE account = %s"
    param01 = [account]
    data01 = select(sql01,param01)
    if len(data01) != 0:
        print("账户存在！！")
        password = input("请输入密码：")
        sql02 = "SELECT passwords FROM user_data WHERE account = %s"
        param02 = [account]
        data02 = select(sql02,param02)
        if data02[0][0] == password:
            print("密码正确！！")
            info = '''
                                 ------------个人信息----------------
                                 账号：%s,
                                 用户名：%s,
                                 取款密码：%s,
                                 地址信息：
                                     国家：%s,
                                     省份：%s,
                                     街道：%s,
                                     门牌号：%s,
                                 余额：%s,
                                 开户行：%s
                                 -----------------------------------
                             '''
            print(
                info % (
                    data01[0][0],
                    data01[0][1],
                    data01[0][2],
                    data01[0][3],
                    data01[0][4],
                    data01[0][5],
                    data01[0][6],
                    data01[0][7],
                    data01[0][8]
                )
            )
        else:
            print("密码错误！！")
    else:
        print("账号不存在！！")

while True:
    welcome()
    num = input("请输入您的业务编号：")
    if num.isdigit():
        num = int(num)
        if num == 1:
            addUser()
        elif num == 2:
            deposite()
        elif num == 3:
            withdraw_money()
        elif num == 4:
            transfer_account()
        elif num == 5:
            query()
        elif num == 6:
            print("拜拜了您嘞，欢迎下次光临！！！")
            break
        else:
            print("输入非法！请重新输入！！！别瞎弄！！！")
    else:
        print("您输入非法！请重新输入！！！")







































