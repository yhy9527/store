
from selenium  import  webdriver
import  time

driver = webdriver.Chrome()

driver.get(r"E:\桌面文件\python自动化测试技术\python自动化测试\selenium\day01\练习的html\上传文件和下拉列表\autotest.html")

#输入用户名过滤数据
driver.find_element_by_xpath("//*[@id='accountID']").send_keys("jason")

# 输入密码
driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("admin")

# 输入地区
driver.find_element_by_xpath("//*[@id='areaID']").send_keys("北京市")

# 性别
driver.find_element_by_xpath("//*[@id='sexID2']").click()

# 四季
driver.find_element_by_xpath("//*[@value='spring']").click()

driver.find_element_by_xpath("//*[@value='Auterm']").click()

# 上传文件
driver.find_element_by_xpath("//input[@name='file' and @type='file']").send_keys(r"C:\Users\jason\Pictures\呸.jpg")

time.sleep(2)

driver.quit()
