*** Settings ***
Library     Selenium2Library
*** Test Cases ***
Тест на сайте Кредитный калькулятор
	Open Browser    https://beregifiguru.ru/%D0%9A%D0%B0%D0%BB%D1%8C%D0%BA%D1%83%D0%BB%D1%8F%D1%82%D0%BE%D1%80%D1%8B/%D0%A0%D0%B0%D1%81%D1%87%D0%B5%D1%82-%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%80%D0%B0-%D0%BE%D0%B4%D0%B5%D0%B6%D0%B4%D1%8B  googlechrome
   	Maximize Browser Window
   	Click Button    xpath=//*[@id="calcFormId"]/button
   	Input Text    id=Height  170
   	Sleep    3seconds
   	Input Text    id=Chest  110
   	Sleep    3seconds
   	Input Text    id=Waist  90
   	Sleep    3seconds
   	Input Text    id=Hips  114
   	Sleep    3seconds
   	Click Button    xpath=/html/body/div[6]/div[2]/div/div/div[2]/form/table/tbody/tr[9]/th/button
	Sleep    5seconds
	Close Browser
