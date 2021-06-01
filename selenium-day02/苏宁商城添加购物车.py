from selenium import webdriver
import time

#创建驱动
driver = webdriver.Chrome()

#访问网站
driver.get("https://www.suning.com/")

#窗口最大化
driver.maximize_window()

time.sleep(3)
#搜索
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("拯救者")
#点击搜索按钮
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()
#点击x
driver.find_element_by_xpath("//*[@id='pop418']/a").click()
#点击商品
driver.find_element_by_xpath("//*[@id='ssdsn_search_pro_baoguang-1-1-1_1_01:0000000000_12110004147-gg']").click()

#获取句柄
wins = driver.window_handles
driver.switch_to.window(wins[1])
#点击加入购物车
driver.find_element_by_xpath("//*[@id='addCart']").click()
#去购物车结算
driver.find_element_by_xpath("/html/body/div[39]/div/div[2]/div/div[1]/a").click()

#关闭界面
driver.quit()

