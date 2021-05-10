# 现在有这样一个叫scores.txt的文件，里面有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。
# 但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致。
# 罗恩 23 35 44
# 哈利 60 77 68 88 90
# 赫敏 97 99 89 91 95 90
# 马尔福 100 85 90
users=[]
f = open(file = "scores.txt",mode = "r+",encoding = "utf-8")
g = open(file = "E:\Program Files (x86)\pythonProject\day10\总分.txt",mode = "w+",encoding="utf-8")
data = f.readlines()
s = 0
for i in data:
    da = i.replace("\n", "").split(" ")  # ["jason","admin","56","男"]
    users.append(da)
    table = users[0+s][1:]
    s+=1
    a = sum(list(map(int, table)))
    g.write(da[0]+"总分："+str(a)+"分"+"\n")








