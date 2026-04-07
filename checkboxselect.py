
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup driver
driver = webdriver.Chrome()
driver.maximize_window()

# Open page
driver.get("https://the-internet.herokuapp.com/checkboxes")

# Find all checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)

check_count=0

for checkbox in checkboxes:
    check_count+=1
    if checkbox.is_selected():
        pass

expected_count=2
if check_count==expected_count:
    print("All checkboxes are checked")
else:
    print("Not all checkboxes are checked")
time.sleep(5)

driver.quit()