print("--------欢迎登录系统--------")
name="root"
password="admin"
count=0
while True:
    a = input("请输入用户名：")
    b = input("请输入密码：")
    if (a!= name or b!= password):
     print("用户名密码输入错误！")
     count = count + 1
    if count == 3:
     print("账户已被锁定！")
     break
