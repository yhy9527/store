from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import time
server = r'http://localhost:4723/wd/hub'      # Appium Server, 端口默认为4723
desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "7.1.2",
        "deviceName": "127.0.0.1:62001",
        "appPackage": "com.tencent.mobileqq",
        "appActivity": "com.tencent.mobileqq.activity.SplashActivity"
    }
driver = webdriver.Remote(server,desired_capabilities)
time.sleep(15)

el1 = driver.find_element_by_accessibility_id("同意")
el1.click()
time.sleep(10)
el2 = driver.find_element_by_id("com.tencent.mobileqq:id/btn_login")
el2.click()
time.sleep(10)
el3 = driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
el3.send_keys("2287962969")
time.sleep(10)
el4 = driver.find_element_by_accessibility_id("密码 安全")
el4.send_keys("8023103yhy...")
time.sleep(10)
el5 = driver.find_element_by_accessibility_id("登 录")
el5.click()