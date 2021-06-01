from selenium import  webdriver
from selenium.webdriver import ActionChains
import  time

driver = webdriver.Chrome()


driver.get("http://www.jd.com")
driver.maximize_window()

# 获取我的京东元素
ele = driver.find_element_by_link_text("我的京东")

# actionchain  事件链
# 将整个页面交给actionchain进行管理。获取管理对象
ac = ActionChains(driver)

# 通过管理对象模拟鼠标和键盘所有操作
ac.move_to_element(ele).perform()  # perform 执行该操作
time.sleep(5)

driver.quit()





