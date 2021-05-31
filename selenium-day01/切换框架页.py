from selenium  import  webdriver
import  time

driver = webdriver.Chrome()

driver.get(r"E:\桌面文件\python自动化测试技术\python自动化测试\selenium\day01\练习的html\main.html")

# 1.切换到id=frame这个框架页里
driver.switch_to.frame("frame")

driver.find_element_by_id("input1").send_keys("65955655")

time.sleep(2)

driver.quit()


