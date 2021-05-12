class User:
    __name = " "
    __sex = " "
    __age = 0
    __huafei = 0
    __brand = " "
    __electricity = 0
    __screen = ""
    __time = ""
    __score = 0

#姓名
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

#性别
    def setSex(self,sex):
        self.__sex = sex
    def getSex(self):
        return self.__sex

#年龄
    def setAge(self,age):
        self.__age = age
    def getaAge(self):
        return self.__age

#手机话费
    def setHuafei(self,huafei):
        self.__huafei = huafei
    def getHuafei(self):
        return self.__huafei

#品牌
    def setBrand(self,brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand

#电池容量
    def setElectricity(self,electricity):
        self.__electricity = electricity
    def getElcetricity(self):
        return self.__electricity

#屏幕
    def setScreen(self,screen):
        self.__screen = screen
    def getScreen(self):
        return self.__screen

#待机时间
    def setTime(self,time):
        self.__time = time
    def getTime(self):
        return self.__time

#积分
    def setScore(self,score):
        self.__score = score
    def getScdore(self):
        return self.__score

#发短信
    def mail(self):
        print("已发送！！！")
    def phone(self):
        num = input("请输入电话号码：")
        time1 = int(input("请输入通话时长："))
        if num.isdigit():
            print("电话已拨通！！")
            if time1 in range(10) :
                self.__huafei=self.__huafei-time1  #话费余额
                self.__score = time1*15#积分
                print("通话：",time1,"分钟","话费余额：",self.__huafei,"积分：",self.__score)
            elif time1 in range(10,21):
                money = 0.8 * time1  # 时长话费
                self.__huafei = self.__huafei - money  # 话费余额
                self.__score = time1 * 39  # 积分
                print("通话：", time1, "分钟", "花费：", money, "元 ", "话费余额：", self.__huafei,"积分：",self.__score)
            elif time1 in range(21,):
                money = 0.65 * time1  # 时长话费
                self.__huafei = self.__huafei - money  # 话费余额
                self.__score = time1 * 48  # 积分
                print("通话：", time1, "分钟", "花费：", money, "元 ", "话费余额：", self.__huafei, "积分：", self.__score)
        elif self.__huafei < 1:
            print("话费不足！！！")
        elif num =="" :
            print("输入为空！！")
        else:
            print("非法输入！！！")

u = User()

u.mail()

u.setName("老王")
u.setHuafei(100)
u.setScore(0)
u.setTime("2天")
u.setAge(23)
u.setBrand("格力")
u.setElectricity(99)
u.setSex("男")
u.phone()