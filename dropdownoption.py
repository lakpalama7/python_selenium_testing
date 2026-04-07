

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.maximize_window()
url="https://the-internet.herokuapp.com/dropdown"
driver.get(url)
dropdown=driver.find_element(By.ID,"dropdown")
select=Select(dropdown)

#select.select_by_visible_text("Option 2")
#value=select.select_by_index(1)
#select.select_by_value("2")
count_options=len(select.options)
print("Number of options in dropdown:",count_options)
expected_count=3

assert count_options==expected_count,"Test Case failed"
print("Test Case passed")
time.sleep(5)