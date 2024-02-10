from telnetlib import EC

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest
import time

from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://mokryinos.ru/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_case_authorization(driver):
    login = driver.find_element(By.XPATH, '/html/body/div[2]/header/div[1]/div/div[3]/a[1]')
    login.click()
    phone = driver.find_element(By.XPATH, '//*[@id="loginform-phone"]')
    phone.click()
    phone.send_keys('9014598765')
    password = driver.find_element(By.XPATH, '//*[@id="loginform-password"]')
    password.click()
    password.send_keys('an1sh190145')
    button = driver.find_element(By.XPATH, '//*[@id="auth-form"]/div[3]/button')
    button.click()

def test_case_search(driver):
    search = driver.find_element(By.XPATH,'//*[@id="top-search-field"]')
    search.click()
    search.send_keys('Grandorf PROBIOTICS Adult Indoor 4 вида мяса с бурым рисом для кошек')
    search.send_keys(Keys.ENTER)
    item = driver.find_element(By.XPATH,'//*[@id="w0"]/li/div/div[1]/div[1]/a/picture/img').get_attribute('alt')
    item_search = 'Grandorf PROBIOTICS Adult Indoor 4 вида мяса с бурым рисом для кошек'
    assert item == item_search

def test_case_basket(driver):
    driver.implicitly_wait(3)
    product_1 = driver.find_element(By.XPATH,'//*[@id="slick-slide12"]/div/li/div/div[4]/div[4]/a')
    product_1.click()
    # в данном месте происходит анимация добавления, которая не дает добавить в корзину повторно
    # не знаю как установить ожидание кроме time.sleep
    time.sleep(1)
    product_1.click()
    product_2 = driver.find_element(By.XPATH, '//*[@id="slick-slide13"]/div/li/div/div[4]/div[4]/a')
    product_2.click()
    basket = driver.find_element(By.XPATH, '/html/body/div[2]/header/div[1]/div/div[3]/a[2]')
    basket.click()
    item_1 = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/input').get_attribute('value')
    item_2 = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[4]/div[1]/input').get_attribute('value')
    assert item_1 == '2'
    assert item_2 == '1'
