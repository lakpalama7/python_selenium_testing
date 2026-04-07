import time
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
# driver.find_element(By.ID,"user-name").send_keys("standard_user")
# driver.find_element(By.ID,"password").send_keys("secret_sauce")

driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[@id='login-button']").click()
expected_url="https://www.saucedemo.com/inventory.html"
actual_url=driver.current_url

# assert expected_url==actual_url,"URL is not matching"
if expected_url==actual_url:
    print("URL is matching")
print(driver.title)
time.sleep(10)
driver.quit()
