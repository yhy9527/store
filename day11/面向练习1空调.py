class Air_conditioner:
    __braned = "  "
    __price = 0

#品牌
    def setBraned(self,braned):
        self.__braned = braned
    def getBraned(self):
        return self.__braned

#价格
    def setPrice(self,price):
        self.__price = price
    def getPrice(self):
        return  self.__price

#开机
    def open(self):
        print(" 空调开机了！！！！！")

#定时关机
    def close(self,time):
        time = int(time)

        print(" 空调将在",time,"分钟后自动关闭！！！！！")

k = Air_conditioner()
k.setBraned("格力")
k.setPrice(6000)
print(" 空调品牌：",k.getBraned(),"\n","空调价格：",k.getPrice(),"元")
k.open()
k.close(30)