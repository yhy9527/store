#属性
class computer:
        __led = " "
        __money = 0
        __cpu = " "
        __neicun = " "
        __time = " "
        # __write = " "
        # __playgame="   "
        # __look=" "
#屏幕
        def setLed(self,led):
            self.__led = led
        def getLed(self):
            return self.__led
#价格
        def setMoney(self,money):
            self.__money = money
        def getMoney(self):
            return self.__money
#cpu
        def setCpu(self,cpu):
            self.__cpu = cpu
        def getCpu(self):
            return self.__cpu
#内存
        def setNeicun(self,neicun):
            self.__neicun = neicun
        def getNeicun(self):
            return self.__neicun
#待机时长
        def setTime(self,time):
            self.__time = time
        def getTime(self,):
            return self.__time
#打字
        def write(self,paper):
            print("用",self.__led,"的电脑",paper)
#打游戏
        def play(self,gamename):
            print("用",self.__cpu,"电脑玩",gamename)
#看视频
        def look(self,videoname):
            print("用",self.__led,"大屏幕看",videoname)

C =computer()
C.setLed("26寸")
C.setCpu("9代i5")
C.setMoney(5000)
C.setNeicun("16G")
C.setTime("10小时")
C.write("敲代码")
C.play("lol")
C.look("电影")














