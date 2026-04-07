
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
baseUrl="https://www.saucedemo.com/"
username="standard_user"
password="secret_sauce"
driver.get(baseUrl)
driver.maximize_window()

username_field=driver.find_element(By.ID,"user-name")
password_field=driver.find_element(By.ID,"password")

username_field.send_keys(username)
password_field.send_keys(password)

login_button=driver.find_element(By.ID,"login-button")

assert not login_button.get_attribute("disabled"),"Login button is disabled"
login_button.click()

# succcess_element=driver.find_element(By.CSS_SELECTOR,".title")
success_element=driver.find_element(By.XPATH,"//span[@class='title']")

assert success_element.text=="Products","Login failed"
print("Login successful")

driver.quit()