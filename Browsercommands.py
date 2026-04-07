


import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.CSS_SELECTOR,".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Username']").send_keys("Sherpa")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(5)
driver.refresh()
driver.quit()
print("Test completed successfully")