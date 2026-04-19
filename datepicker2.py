
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from datetime import datetime, timedelta

from selenium.webdriver.support.ui import Select



driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.find_element(By.XPATH,"//input[@id='datepicker2']").click()
time.sleep(5)

current_time=datetime.now()
print("Current time:",current_time)

next_day=current_time+timedelta(days=1)
print("Next day:",next_day.day)
Next_day=str(next_day.day)

current_month=datetime.now().month
current_year=current_time.year
next_month=(current_month % 12)+2

next_month_year=f"{next_month}/{current_year}"

dropdown_month=driver.find_element(By.CSS_SELECTOR,"select[title='Change the month']")
select=Select(dropdown_month)
select.select_by_value(str(next_month_year))

dropdown_year=driver.find_element(By.XPATH,"//select[@title='Change the year']")
select_year=Select(dropdown_year)
select_year.select_by_visible_text("2027")

driver.find_element(By.LINK_TEXT,Next_day).click()


time.sleep(5)