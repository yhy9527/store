
f1 = open(file="E:\桌面文件\python自动化测试技术\python\day10\代码\day10\景甜.jpg",mode="rb")
f2 = open(file="D:\python\景甜2.jpg",mode="wb")

data = f1.read()
f2.write(data)

f2.close()
f1.close()












