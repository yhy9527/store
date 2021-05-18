'''
    多线程：
        进程：一个正在进行的程序：进程
        线程：就是属于某个进程下的子功能。
    任务：
        电脑管家杀毒：
            任务：杀毒
        360管家杀毒
        前提：一起杀毒
    实现：thread
        1.子类继承threading类
        2.重写run方法：在run方法里写入任务代码。
'''
import threading
import time
class PCmanager(threading.Thread): # 电脑管家

    def run(self) -> None:
        for i in range(100):
            time.sleep(0.5)
            print("电脑管家正在杀毒，已经杀了",i,"个毒！")

class Manager360(threading.Thread):  # 360 管家

    def run(self) -> None:
        for i in range(100):
            time.sleep(0.5)
            print("360奇虎正在杀毒，已经杀了", i, "个毒！")
pc = PCmanager()
manager = Manager360()
# 调用start方法完成线程的开启
pc.start()  # 电脑管家开始杀毒
manager.start() # 360管家开始杀毒




























