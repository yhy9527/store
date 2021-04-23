#普通版
list = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
print("共有：",len(list),"个数字")
print("1出现的次数：",list.count(1),"次")
print("4出现的次数：",list.count(4),"次")
print("7出现的次数：",list.count(7),"次")
print("5出现的次数：",list.count(5),"次")
print("8出现的次数：",list.count(8),"次")
print("2出现的次数：",list.count(2),"次")
print("3出现的次数：",list.count(3),"次")
print("9出现的次数：",list.count(9),"次")
print("6出现的次数：",list.count(6),"次")
print("10出现的次数：",list.count(10),"次")

#进阶版
list = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
liset=set(list)
for i in liset:
    print("数字",i,"出现",list.count(i),"次。")
