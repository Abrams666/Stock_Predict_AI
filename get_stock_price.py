#imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium
import time
#config
PATH="D:/Stock AI/chromedriver-win64/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.twse.com.tw/zh/trading/historical/stock-day.html")
#search
stock_no=driver.find_element(By.NAME,"stockNo")
stock_no.send_keys("2330")
stock_no.send_keys(Keys.RETURN)

time.sleep(3)