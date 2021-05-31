from selenium import webdriver
import time

#创建驱动
driver = webdriver.Chrome()

#打开网页
driver.get("E:\桌面文件\python自动化测试技术\python自动化测试\selenium\day01\练习的html\跳转页面\pop.html")

#窗口最大化
driver.maximize_window()

#定位输入
driver.find_element_by_id("goo").click()

#等待两秒
time.sleep(2)

#退出浏览器
driver.quit()



















