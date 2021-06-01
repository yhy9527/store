from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.taobao.com")

time.sleep(10)

#输入苹果12
driver.find_element_by_xpath("//*[@id='q']").send_keys("苹果12")

#手动扫码登录
#点击搜索
driver.find_element_by_xpath("//*[@id='J_TSearchForm']/div[1]/button").click()

#选择商品
driver.find_element_by_xpath("//*[@id='J_Itemlist_TLink_632908182243']").click()

#选择商品规格

driver.find_element_by_xpath("//*[@id='J_DetailMeta']/div[1]/div[1]/div/div[4]/div/div/dl[1]/dd/ul/li/a").click()
driver.find_element_by_xpath("//*[@id='J_DetailMeta']/div[1]/div[1]/div/div[4]/div/div/dl[4]/dd/ul/li[2]/a").click()

#加入购物车
driver.find_element_by_xpath("//*[@id='J_LinkBasket']").click()
