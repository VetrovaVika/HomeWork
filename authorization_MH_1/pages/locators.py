# Locators.py - содержит локаторы на всех страницах сайта Мокрый Нос
from selenium.webdriver.common.by import By

# Локаторы авторизации
authorization = (By.XPATH, '/html/body/div[2]/header/div[1]/div/div[3]/a[1]')
telephone = (By.XPATH, '//*[@id="loginform-phone"]')
password = (By.XPATH, '//*[@id="loginform-password"]')
button = (By.XPATH, '//*[@id="auth-form"]/div[3]/button')