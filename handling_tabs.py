
import time

from selenium import webdriver

from brokenimages import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/")
driver.switch_to.new_window()
driver.get("https://playwright.dev/")
number_tab=len(driver.window_handles)
print("Number of tabs opened: ",number_tab)
time.sleep(2)

tab_value=driver.window_handles
print(tab_value)

current_window_tab=driver.current_window_handle
print(current_window_tab)

driver.find_element(By.CSS_SELECTOR,".getStarted_Sjon").click()

first_window_tab=tab_value[0]

if current_window_tab!=first_window_tab:
    driver.switch_to.window(first_window_tab)

driver.find_element(By.XPATH,"//span[normalize-space()='Downloads']").click()

time.sleep(2)

driver.quit()