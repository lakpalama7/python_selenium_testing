

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

url="https://jqueryui.com/"

driver=webdriver.Chrome()
driver.maximize_window()
driver.get(url)
total_links=driver.find_elements(By.TAG_NAME,"a")
print(total_links)
print(f"Total links on the page is : {len(total_links)}")

for link in total_links:
    href=link.get_attribute("href")
    if href:
        response_code=requests.get(href)
        if response_code.status_code >= 400:
            print(f"Broken link:{href}(Status code:{response_code.status_code})")

driver.quit()