'''
    1~10:纯写代码
        程序结构：
            顺序结构
            选择结构
            循环结构
        函数
面向过程：
    就是将所有过程进行大致罗列，进行编程。
面向对象：
    C,C++: pymysql底层驱动，网卡驱动，面向过程语句。
    java,python：面向对象。
    核心思想：指挥对象去干事情。
事务：造车。
    1.画一张车图纸。
        类：class
    2.在工厂里真正造一辆车。
        类()
    3.优化数据。
车：
    轮胎数，车身颜色，座位数，车型号，重量    属性
    跑，拉货 (本质就是一个函数，方法)                                     行为
'''
class Car:  # 1.用class 描述一辆车
    # 属性与行为
    num = 0
    color = ""
    sites = ""
    brand = ""
    weight = 0

    def run(self):
        print(self.brand , "正在大马路上跑来跑去！！！溜了溜了！！")

c = Car() # 2.造一辆车
# 3. 给车赋值
c.num = 3
c.color = "绿色"
c.sites = 6
c.weight = "300kg"
c.brand = "宝马A6"
# 4.调用车的方法，让车完成一些功能
c.run()
#  任务：分析人具有的属性和行为并用代码实现



class men:
    name = ""
    age = 0
    sex = " "
    height = 0
    weight = 0
    def play(self):
        print("一个人正在玩！！")
a = men()
#给人赋值
name="小明"
age = 23
sex= "boy"
height = 185
weight = 80
a.play()











