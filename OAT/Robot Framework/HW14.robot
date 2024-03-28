*** Settings ***
Library           SeleniumLibrary

*** Keywords ***
Calculate consumption and cost
    [Arguments]    ${consumption}     ${distance}     ${cost}     ${result}
    Open Browser        https://calcus.ru/kalkulyator-rashoda-topliva    Chrome
    Click Element    xpath=(.//*[normalize-space(text()) and normalize-space(.)='Английские (мили, галлоны)'])[1]/following::label[1]
    Input Text    name=average_consumption    ${consumption}
    Input Text    name=distance    ${distance}
    Input Text    name=cost    ${cost}
    Click Button    xpath=/html/body/div[2]/div[2]/div[1]/form/div[15]/div/input
    Sleep    5sec
    ${result_field}    Get Text    xpath=/html/body/div[2]/div[2]/div[1]/form/div[12]/div[2]/div
    Should be Equal    ${result}    ${result_field}
    Sleep    3sec
    Close Browser

Calculate average consumption per 100 km
    [Arguments]    ${consumption}     ${distance}     ${cost}     ${result}
    Open Browser        https://calcus.ru/kalkulyator-rashoda-topliva    Chrome
    Click Element    xpath=(.//*[normalize-space(text()) and normalize-space(.)='Рассчитать расход и стоимость'])[1]/following::label[1]
    Input Text    name=consumption    ${consumption}
    Input Text    name=distance    ${distance}
    Input Text    name=cost    ${cost}
    Click Button    xpath=/html/body/div[2]/div[2]/div[1]/form/div[15]/div/input
    Sleep    5sec
    ${result_field}    Get Text    xpath=/html/body/div[2]/div[2]/div[1]/form/div[13]/div[2]/div[1]
    Should be Equal    ${result}    ${result_field}
    Sleep    3sec
    Close Browser


*** Test Cases ***
Положительные числа: 
    Calculate consumption and cost    100    2    10    2
    Calculate average consumption per 100 km    10    2    30    500
    # пройдено

Ноль:
    Calculate consumption and cost    0    0    0    error
    Calculate average consumption per 100 km    0    0    0    error
    # ошибка, т.к. поле ${distance} не может быть нулем

Дополнительная проверка на ноль:
    Calculate consumption and cost    0    2    1    error
    Calculate average consumption per 100 km    0    2    1    error
    # ошибка, т.к. поле ${consumption} не может быть нулем

Дроби:
    Calculate consumption and cost    2,5    3,4    5,6    error
    Calculate average consumption per 100 km    2,5    3,4    5,6    error
    # ошибка, т.к. поле ${distance} не может быть дробным

Дополнительная проверка на дроби:
    Calculate consumption and cost    2,5    3    5,6    0,08
    Calculate average consumption per 100 km    2,5    3    5,6    83,33
    # пройдено

Отрицательные:
    Calculate consumption and cost   -8    7    7    0
    Calculate average consumption per 100 km    -8    7    7    0
    # ошибка, т.к. производится отрицательный рассчет

Пустые:
    Calculate consumption and cost    ${EMPTY}    ${EMPTY}    ${EMPTY}    error
    Calculate average consumption per 100 km    ${EMPTY}    ${EMPTY}    ${EMPTY}    error
    # ошибка, т.к. поля обязательны для заполнения

