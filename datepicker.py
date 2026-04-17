

from datetime import datetime, timedelta
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.globalsqa.com/demo-site/datepicker/")

frame=driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//iframe[@class='demo-frame']")
driver.switch_to.frame(frame)
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"#datepicker").click()

current_time=datetime.now()

target_time=current_time+timedelta(days=1)

format_date=target_time.strftime("%m/%d/%Y")
driver.find_element(By.CSS_SELECTOR,"#datepicker").send_keys(format_date + Keys.TAB)
time.sleep(5)
driver.quit()