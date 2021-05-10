'''
    先读后写：
    r+,w+
'''
f1 = open(file="古诗.txt",mode="r+",encoding="utf-8")
f2 = open(file="b.txt",mode="w+",encoding="utf-8")

data = f1.read()
f2.write(data)

f2.close()
f1.close()






