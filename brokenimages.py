

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.maximize_window()
url ="https://the-internet.herokuapp.com/broken_images"
driver.get(url)
image_tag=driver.find_elements(By.TAG_NAME,"img")

broken_images = []
for image in image_tag:
    src=image.get_attribute("src")
    if src:
        response_code=requests.get(src)
        if response_code.status_code != 200:
            broken_images.append(src)
            print("Broken image found: ")

print(f"Total broken images on the page is : {len(broken_images)}")
if broken_images:
    for image in broken_images:
        print(image)

driver.quit()