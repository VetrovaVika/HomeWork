from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_select_customer(driver):
    try:
        Customer_Login = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[1]/button")
        Customer_Login.click()
        customer_dropdown = Select(driver.find_element(By.XPATH, "//select[@ng-model='custId']"))
        customer_dropdown.select_by_visible_text("Hermoine Granger")
        selected_customer = customer_dropdown.first_selected_option.text
        assert selected_customer == "Hermoine Granger"
        Login = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/button")
        Login.click()
    except NoSuchElementException:
        print('Элемент не найден')

def test_dont_select_customer(driver):
    Customer_Login = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[1]/button")
    Customer_Login.click()
    try:
        element = driver.find_element(By.CLASS_NAME, "btn btn-default ng-hide")
        element.click()
    except NoSuchElementException:
        print("Элемент не найден")