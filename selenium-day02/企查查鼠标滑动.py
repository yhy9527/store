from selenium import  webdriver
from selenium.webdriver import ActionChains
import  time
#创建驱动
driver = webdriver.Chrome()

#访问网址
driver.get("https://www.qcc.com")
#窗口最大化
driver.maximize_window()

time.sleep(6)
# 取消框
driver.find_element_by_xpath("//*[@id='addfavorModal']/div/div/div[1]").click()
#//*[@id="addfavorModal"]/div/div/div[1]/img[2]

# 点击登陆
driver.find_element_by_link_text("登录 | 注册").click()
time.sleep(5)

# 获取滑块
ele = driver.find_element_by_xpath("//*[@id='nc_1_n1z']")

# 创建Actionchain
ac = ActionChains(driver)

ac.click_and_hold(ele).move_by_offset(348,0).perform()


time.sleep(5)

driver.quit()
