# encoding=utf-8
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import time

server = r'http://localhost:4723/wd/hub'      # Appium Server, 端口默认为4723
desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "7.1.2",
        "deviceName": "127.0.0.1:62001",
        "appPackage": "com.jingdong.app.mall",
        "appActivity": "com.jingdong.app.mall.main.MainActivity"
    }
driver = webdriver.Remote(server, desired_capabilities) # 连接手机和APP
time.sleep(20)
TouchAction(driver).tap(x=347, y=189).perform()
time.sleep(5)
#输入背包
el1 = driver.find_element_by_id("com.jd.lib.search.feature:id/a3g").send_keys("背包")
time.sleep(5)
#点击搜索按钮
TouchAction(driver).tap(x=839, y=106).perform()

time.sleep(5)
TouchAction(driver).tap(x=120, y=831).perform()
time.sleep(5)
#加入购物车
TouchAction(driver).tap(x=544, y=1547).perform()

time.sleep(5)
TouchAction(driver).tap(x=228, y=772).perform()
time.sleep(5)
TouchAction(driver).tap(x=490, y=1546).perform()
time.sleep(5)
TouchAction(driver).tap(x=362, y=1548).perform()