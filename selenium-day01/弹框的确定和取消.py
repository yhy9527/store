
from selenium  import  webdriver
import  time

driver = webdriver.Chrome()

driver.get(r"E:\桌面文件\python自动化测试技术\python自动化测试\selenium\day01\练习的html\弹框的验证\dialogs.html")

driver.find_element_by_id("confirm").click()
time.sleep(2)
#切换到弹框里
driver.switch_to.alert.dismiss()  # accept 点击确定    dismiss  点击取消

time.sleep(2)

driver.quit()
