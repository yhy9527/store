class Cooker:
    __name = ""
    __age = ""

#姓名
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
#年龄
    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age


    def rice(self):
        print("正在做饭！")

class Cook1(Cooker):
    def cook2(self):
        print("正在炒菜！！！")

class Cook2(Cooker):
    def cook3(self):
        print("蒸饭！！！")
    def cook4(self):
        print("炒菜！！！")



class Test():
    C = Cooker()
    C.setAge(26)
    C.setName("小明")
    print(C.getName(), C.getAge())
    C.rice()
    C1 = Cook1()
    C1.cook2()









