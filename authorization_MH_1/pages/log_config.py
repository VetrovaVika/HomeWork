import logging

logger = logging.getLogger(__name__)

# настройка обработчика и форматировщика для logger2
handler = logging.FileHandler(f"MH_log.log", mode='w', encoding="utf-8")
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

# добавление форматировщика к обработчику
handler.setFormatter(formatter)

# добавление обработчика к логгеру
logger.addHandler(handler)

logger.setLevel(logging.INFO)

def data_login(data):
    for i, l in enumerate(data):
        data[i] = (l['telephone'], l['password'], l['expected_result'])
    logger.info('Cформированы тест-кейсы')
    return data

test_cases = [
    {
        "description": "Успешный вход с правильными учетными данными",
        "telephone": "9014598765",
        "password": "an1sh190145",
        "expected_result": ""
    },
    {
        "description": "Вход с неверными учетными данными",
        "telephone": "3598741569",
        "password": "invalidpassword",
        "expected_result": "site/login"
    },
    {
        "description": "Вход с пустым полем пароля",
        "telephone": "9014598765",
        "password": "",
        "expected_result": "site/login"
    },
    {
        "description": "Вход с пустым полем телефон",
        "telephone": "",
        "password": "an1sh190145",
        "expected_result": "site/login"
    },
    {
        "description": "Вход с пустыми полями",
        "telephone": "",
        "password": "",
        "expected_result": "site/login"
    },
    {
        "description": "Вход с неправильным форматом телефон",
        "telephone": "@#%$^",
        "password": "an1sh190145",
        "expected_result": "site/login"
    },
]
