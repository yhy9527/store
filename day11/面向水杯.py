class cup:
    __height = " "
    __room = " "
    __color = " "
    __material = " "

    def setHeight(self,height):
        self.__height = height
    def getHeight(self):
        return  self.__height

    def setRoom(self,room):
        self.__room = room
    def getRoom(self):
        return self.__room

    def setColor(self,color):
        self.__color = color
    def getColor(self,color):
        return self.__color

    def setMaterial(self,material):
        self.__material = material
    def getmasterial(self):
        return self.__material
    def show(self):
        print("高度:",self.__height,"\n",
              "容量:",self.__room,"\n",
              "颜色:",self.__color,"\n",
              "材质:",self.__material)

C = cup()
C.setHeight("60g")
C.setRoom("500ml")
C.setColor("红色")
C.setMaterial("玻璃")
C.show()

















