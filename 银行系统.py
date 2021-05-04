import random
# 1. 空的银行的数据库 ： 100个
users = {}

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
    if len(users) >= 100:
        return 3

    # 判断是否存在
    if account in users:
        return 2

    #正常开户
    users[account] = {
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":0,
        "bank_name":bank_name
    }
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
    # 余额不允许第一次输入，需要存钱

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
        print(info % (account,name,password,country,province,street,door,users[account]["money"],bank_name))

    elif status == 2:
        print("对不起，该用户已存在！请稍后重试！！！")
    elif status == 3:
        print("对不起，该银行库已满，请携带证件到其他银行办理！！！")


#存钱
def deposite():
    zh = input("请输入用户账号：")
    if zh in users:
        print("用户存在")
        je = int(input("请输入存钱金额："))
        users[zh]["money"] += je
        print("存钱成功！！您的余额：",users[zh]["money"])
    else:
        return print("用户不存在！！")

#取钱
def withdraw_money():
    zh = input("请输入用户账号：")
    if zh in users.keys() :
        print("账户存在！")
        password = input("请输入密码：")
        if password == users[zh]["password"] :
            print("密码正确！")
            qqje = int(input("请输入取钱金额："))
            if qqje <= users[zh]["money"]:
                users[zh]["money"] = users[zh]["money"] - qqje
                print("取钱成功！！您的余额：",users[zh]["money"])
            else:
                print("余额不足！！")
        else:
            print("密码错误！")
    else:
        print("账户不存在！！")

#转账
def transfer_account():
    a = input("请输入转出账号：")
    b = input("请输入转入账号：")
    if a in users.keys() and b in users.keys():
        print("账号存在！")
        password = input("请输入转出账号密码：")
        if password == users[a]["password"]:
            print("密码正确！")
            zcje = int(input("请输入转出金额："))
            if  users[a]["money"] >= zcje :
                users[a]["money"] -= zcje
                users[b]["money"] +=  zcje
                print("转账成功！！")
                print("转出金额：",zcje,"\n",
                      "账户：",a,"余额：",users[a]["money"],"\n",
                      "账户：", b, "余额：", users[b]["money"],"\n",
                       )
            else:
                print("钱不够！！！")
        else:
            print("密码错误！！")
    else:
        print("转入或转出账号不存在！")
#查询
def query():
    account_number = input("请输入用户账号：")
    if account_number in users.keys():
        print("用户存在")
        password = input("请输入密码：")
        if password == users[account_number]["password"]:
            print("密码正确！")
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
            print(info % (account_number,users[account_number]["username"], users[account_number]["password"],
                users[account_number]["country"], users[account_number]["province"],
                 users[account_number]["street"], users[account_number]["door"],
                          users[account_number]["money"] , bank_name))
        else:
            print("密码错误！")
    else:
            print("用户不存在！")

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







































