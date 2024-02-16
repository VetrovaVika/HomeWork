from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://mokryinos.ru/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.parametrize("input_value", [("Grandorf"), ("Asdfergw"), ("Fiori")])
def test_case_search_comparison(driver, input_value):
    search = driver.find_element(By.XPATH,'//*[@id="top-search-field"]')
    search.click()
    search.send_keys(input_value)
    search.send_keys(Keys.ENTER)
    div_elem = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div')
    if int(div_elem.text) > 0:
        print('\n количество найденных совпадений:', div_elem.text)
    else:
        print('\n ничего не найдено')

# assert div_elem.text == '30'
# assert int(results.text) > 0
