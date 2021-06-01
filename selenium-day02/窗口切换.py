from selenium  import  webdriver
import  time
driver = webdriver.Chrome()


driver.get(r"E:\桌面文件\python自动化测试技术\python自动化测试\selenium\day01\练习的html\跳转页面\pop.html")

driver.maximize_window()

time.sleep(1)

driver.find_element_by_xpath("//*[@id='goo']").click()

# 切换窗口
# 获取所有窗口句柄生成一个列表
wins = driver.window_handles  # ["asdf105as1fa50ds1fa5df","1a05sd1fa651f6as5f1a65df"]
print(wins)
# 切换操作窗口列表中的第一个
driver.switch_to.window(wins[1])

driver.find_element_by_xpath("//*[@id='kw']").send_keys("java")

driver.find_element_by_xpath("//*[@id='su']").click()

time.sleep(3)

driver.switch_to.window(wins[0])

driver.quit()










