from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.python.org/")
elem = driver.find_element(By.ID, "id-search-field")
elem.click()
elem.send_keys("input")
elem.send_keys(Keys.ENTER)
time.sleep(5)
driver.save_screenshot("screenshot.png")
current_url = driver.current_url
print(current_url)
elem = driver.find_element(By.ID, "id-search-field")
elem.click()
elem.clear()
elem.send_keys("print")
elem.send_keys(Keys.ENTER)
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.quit()
