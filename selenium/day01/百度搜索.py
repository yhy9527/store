from selenium import webdriver
import time

#创建驱动
driver = webdriver.Chrome()

#打开网页
driver.get("http://www.baidu.com")

#窗口最大化
driver.maximize_window()

#定位输入框，并输入java
driver.find_element_by_id("kw").send_keys("java")

#点击百度一下
driver .find_element_by_id("su").click()  #click点击

#等待两秒

time.sleep(3)

#退出浏览器
driver.quit()














