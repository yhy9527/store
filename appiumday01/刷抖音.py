from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction


server = r'http://localhost:4723/wd/hub'
desired_caps = {
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.ss.android.ugc.aweme",
  "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity"
}

driver = webdriver.Remote(server, desired_caps) # 连接手机和APP
time.sleep(5)
#按道理来说是可以的
TouchAction(driver).press(x=472, y=1174).move_to(x=472, y=722).wait(2).release().perform()
time.sleep(5)
TouchAction(driver).press(x=472, y=1174).move_to(x=472, y=722).wait(2).release().perform()
time.sleep(5)
TouchAction(driver).press(x=472, y=1174).move_to(x=472, y=722).wait(2).release().perform()
time.sleep(5)
TouchAction(driver).press(x=472, y=1174).move_to(x=472, y=722).wait(2).release().perform()
time.sleep(5)