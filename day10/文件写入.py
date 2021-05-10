'''
    存储数据：
        1.变量
        2.元组，列表，字典，集合
        3.数据库：mysql   (pymysql)
        4.文件读写：.txt  （python提供了对文件读写）
    1. 打开文件
        模式：
            r、w、b(图片、MP3、mp4),a(附加)，+可读可写
    2. 写入数据
    3. 关闭资源
'''


#打开
f = open(file = "古诗.txt",mode="r+",encoding="utf-8")

#写入数据
f.write("咏鹅\n")
f.write("鹅鹅鹅\n")
f.write("曲项向天歌\n")
f.write("白毛浮绿水\n")
# print(f.read())
# print(f.readline())  一次打印一行

# f.readlines() # ["静夜思","【李白】",""]
print(f.readline())
#关闭资源
f.close()












