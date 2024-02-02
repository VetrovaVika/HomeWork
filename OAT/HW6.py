from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://calcus.ru/kalkulyator-ipoteki")
try:
    PropertyValue = driver.find_element(By.NAME, 'cost')
    PropertyValue.click()
    PropertyValue.send_keys('4750000')
    AnInitialFee = driver.find_element(By.NAME, 'start_sum')
    AnInitialFee.click()
    AnInitialFee.send_keys('950000')
    CreditTerm = driver.find_element(By.NAME, 'period')
    CreditTerm.click()
    CreditTerm.send_keys('20')
    InterestRate = driver.find_element(By.NAME, 'percent')
    InterestRate.click()
    InterestRate.send_keys('4,7')
    InterestRate.send_keys(Keys.ENTER)
    # Не разобралась как нажатие на кнопку сделать, код ниже не работал, поэтому через ENTER
    # driver.implicitly_wait(5)
    # button = driver.find_element(By.CLASS_NAME, "calc-submit me-3")
    # button.click()
    driver.save_screenshot('mortgage_calculator.png')
except NoSuchElementException:
    print('Что-то пошло не так')
