#imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#config
driver = webdriver.Chrome()
driver.get("https://www.twse.com.tw/zh/trading/historical/stock-day.html")

#search
stock_no = driver.find_element(By.NAME, "stockNo")
stock_no.send_keys("2330")
stock_no.send_keys(Keys.RETURN)

search=driver.find_elements(By.CLASS_NAME, "search")
search[2].click()

time.sleep(3)