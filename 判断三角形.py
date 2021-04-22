a=int(input("请输入三角形第一条边："))
b=int(input("请输入三角形第二条边："))
c=int(input("请输入三角形第三条边："))
if (a+b>c) and (b+c>a) and (a+c>b):
    if a==b==c:
       print("等边三角形")
    elif  a==b or b==c or a==c:
       print("等腰三角形")
    elif (a**2+b**2==c**2) or (b**2+c**2==a**2) or (a**2+c**2==b**2):
       print("直角三角形")
    else:
        print("普通三角形")
else:
    print("不是三角形")
