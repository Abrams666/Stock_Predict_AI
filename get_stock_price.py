#imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

#config
driver = webdriver.Chrome()
driver.get("https://www.twse.com.tw/zh/trading/historical/stock-day.html")

#search
stock_no = driver.find_element(By.NAME, "stockNo")
stock_no.send_keys("2330")

for i in range(99,114):
    for j in range(1,13):
        year_select=driver.find_element(By.NAME,"yy")
        year_option=Select(year_select)
        year_option.select_by_visible_text("民國 "+ str(i) +" 年")
        
        month_select=driver.find_element(By.NAME,"mm")
        month_option=Select(month_select)
        if (len(str(j))==1):
            month_option.select_by_visible_text("0"+str(j) +"月")
        elif(len(str(j))==2):
            month_option.select_by_visible_text(str(j) +"月")

        search=driver.find_elements(By.CLASS_NAME, "search")
        search[2].click()

        time.sleep(1)

        download=driver.find_element(By.CLASS_NAME,"csv")
        download.click()
        print("Data "+str(i)+"/"+str(j)+" downloaded")

        time.sleep(2)