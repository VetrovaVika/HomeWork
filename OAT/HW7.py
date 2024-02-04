import requests

def test_status_code_200():
    date = '2024-01-01'
    url = f'https://api.nasa.gov/planetary/apod?api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla&date={date}'
    response = requests.get(url)
    result = response.status_code
    assert 200 <= result < 400
def test_status_code_200():
    date = '2024-02-04'
    url = f'https://api.nasa.gov/planetary/apod?api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla&date={date}'
    response = requests.get(url)
    result = response.status_code
    assert 200 <= result < 400
def test_status_code_400():
    date = '2025-01-01'
    url = f'https://api.nasa.gov/planetary/apod?api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla&date={date}'
    response = requests.get(url)
    result = response.status_code
    assert 200 <= result <= 400