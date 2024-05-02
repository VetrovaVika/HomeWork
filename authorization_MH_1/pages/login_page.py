from .locators import *
from .log_config import *
import time

class LoginPage:
    def __init__(self, browser):
        time.sleep(3) # Ожидание кнопки
        self.open_btn = browser.find_element(*authorization)
        self.open_btn.click()
        logger.info('Найдена кнопка авторизации/регистрации')

        time.sleep(2) # Ожидание пока появиться форма
        self.telephone = browser.find_element(*telephone)
        self.password = browser.find_element(*password)
        self.button = browser.find_element(*button)
        logger.info('Все элементы на страницы были найдены')

    def login(self, telephone: str = '', password: str = ''):
        logger.info('Начало авторизации')
        self.telephone.send_keys(telephone)
        self.password.send_keys(password)
        self.button.click()
        time.sleep(2) # Ожидание сравнения url
        logger.info('Конец авторизации')


