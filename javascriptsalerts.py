

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
url="https://the-internet.herokuapp.com/javascript_alerts"
driver.get(url)

alert_button=driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")
alert_button.click()

alert=driver.switch_to.alert
print("Alert text is :",alert.text )
time.sleep(2)

alert.send_keys("Jyvaskla")
time.sleep(2)
alert.accept()

#alert.dismiss()
time.sleep(2)

driver.quit()
                                 