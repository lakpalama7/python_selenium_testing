

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")

iframe=driver.find_element(By.ID,"mce_0_ifr")
driver.switch_to.frame(iframe)

text_editor=driver.find_element(By.ID,"tinymce")
text_editor.clear()

text_editor.send_keys("Hello, this is a testing message for text editor inside an iframe.")

time.sleep(5)

driver.find_element(By.XPATH,"//a[normalize-space()='Elemental Selenium']").click()
driver.quit()

