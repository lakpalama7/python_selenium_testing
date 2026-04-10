

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/tables")
driver.maximize_window()
driver.execute_script("window.scrollTo(0,700)")

table=driver.find_element(By.ID,"table1")
rows=table.find_elements(By.TAG_NAME,"tr")
row_count=len(rows)
print(f"Number of rows in the table: {row_count}")

target_value="jsmith@gmail.com"
found = False
for row in rows:
    cells=row.find_elements(By.TAG_NAME,"td")

    for cell in cells:
        if target_value in cell.text:
            print(f"Target Value is : {target_value}")
            found = True
            break
    if found:
        break

if not found:
    print(f"Target Value '{target_value}' not found in the table.")


time.sleep(5)
driver.quit()