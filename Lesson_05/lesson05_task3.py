from selenium import webdriver

from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

#Переход на страницу
driver.get("http://the-internet.herokuapp.com/inputs")
    
#Находим поле ввода
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
    
#Вводим текст "Sky"
input_field.send_keys("Sky")
sleep(5)
    
#Очищаем поле
input_field.clear()
sleep(5)
    
#Вводим текст "Pro"
input_field.send_keys("Pro")
sleep(5)

#Закрываем браузер
driver.quit()