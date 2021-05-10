path  = input("请输入上传图片的路径：")
f1 = open(file=path,mode="rb")
f2 = open(file="D:\python\景甜2.jpg",mode="wb")
data = f1.read()
f2.write(data)
print("上传成功！！")
f2.close()
f1.close()




