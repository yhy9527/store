


f1 = open(file="景甜.jpg",mode="rb")
f2 = open(file="景甜2.",mode="wb")

data = f1.read()
f2.write(data)

f2.close()
f1.close()
