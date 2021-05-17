class Person:
    __age = None
    __sex = None
    __name = None

    def setAge(self,age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setSex(self,sex):
        self.__sex = sex

    def getSex(self):
        return self.__sex

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name

# 工人
class Worker(Person):

    def work(self):
        print(self.getName(),"正在干活!")

# 学生
class Student(Person):
    __sid = None

    def setSid(self,sid):
        self.__sid = sid
    def getSid(self):
        return self.__sid






