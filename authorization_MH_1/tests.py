from config import *


@pytest.mark.parametrize('telephone, password, expected_url', data_login(test_cases))
def test_login_page(browser, telephone, password, expected_url):
    logger.info(f"Начало теста test_login_page")
    login_page = LoginPage(browser)
    login_page.login(telephone, password)
    assert browser.current_url == base_url + expected_url
    logger.info(f"Конец теста test_login_page")