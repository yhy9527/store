from DBUtils import update
from DBUtils import select
users=[]
f = open(file = "user.txt",mode="r+",encoding="gbk")
data = f.readlines()
q = 0
for i in data:
    da = i.replace("\n","").split(",")
    users.append(da)
    sql = "INSERT INTO USER VALUE(%s,%s,%s);"
    param = [users[0+q][0],users[0+q][1],users[0+q][2]]
    q = q+1
    update(sql,param)
    print("插入数据成功！！")
sql01 = "SELECT SUM(净资产) FROM USER;"
param =[]
data = select(sql01,param)
print("总资产：",data[0][0])


