# config.py - содержит все необходимые настройки для тестирования
import pytest
from selenium import webdriver
from pages.login_page import * #изменила способ подключения

# Настройка опций для headless режима
#chrome_options = Options()
#chrome_options.add_argument("--headless") # не получится тестировать в таком режиме из-за js

# Инициализация WebDriver с указанием опций
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
base_url = 'https://mokryinos.ru/'

@pytest.fixture(scope="function")
def browser():
    driver.get(base_url)
    logger.info(f"Была открыта ссылка {base_url}")
    driver.implicitly_wait(5)
    yield driver
    #driver.get('https://mokryinos.ru/site/logout')
    logger.info(f"Конец фикстуры")