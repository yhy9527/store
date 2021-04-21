id = input("请输入身份证号：")
name =input ("请输入姓名：")
age = input ("请输入年龄：")
sex=input ("请输入性别：")
height = input("请输入身高：")
addr = input("请输入居住地址：")
info = '''
*************个人信息**************
身份证号：%s
姓   名：%s
年   龄：%s
性   别：%s
身   高：%s
居住地址：%s
**********************************
      '''
print(info % (id,name,age,sex,height,addr))