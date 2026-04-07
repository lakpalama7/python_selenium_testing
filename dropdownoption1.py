

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
driver.maximize_window()
url="https://the-internet.herokuapp.com/dropdown"
driver.get(url)
dropdown=driver.find_element(By.ID,"dropdown")
select=Select(dropdown)

target_value="Option 1"

for option in select.options:
    if option.text==target_value:
        option.click()
        print("Option found and selected:",target_value)
        break
  
    else:
        print("Option not found:",target_value)
time.sleep(5)
driver.quit()
