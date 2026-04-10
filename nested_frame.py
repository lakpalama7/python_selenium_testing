

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/nested_frames")

# Switch to the top frame
driver.switch_to.frame("frame-top")
# Switch to the middle frame
driver.switch_to.frame("frame-middle")

content=driver.find_element(By.ID,"content")
print(f"The content of the middle frame is: {content.text}")
driver.switch_to.default_content() # switch back to the main page
# switch to bottom frame
driver.switch_to.frame("frame-bottom")
bottom_content=driver.find_element(By.TAG_NAME,"body")
print(f"The content of the bottom frame is: {bottom_content.text}")

time.sleep(2)
driver.quit()
