class Oldphone:

    __brand = " "
#品牌
    def setBrand(self,brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand


    def Phone(self):
        print("正在给：",self.__brand,"手机打电话！")

class Newphone(Oldphone):
    def call(self):
        print("语音拨号中。。。")
        super().Phone()
C = Oldphone()
C.setBrand("小米牌")
C.Phone()
n=Newphone()
n.setBrand("tttt")
n.call()


















