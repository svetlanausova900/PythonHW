from selenium import webdriver

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

#Инициализация драйвера Firefox
driver = webdriver.Firefox()


driver.get("http://the-internet.herokuapp.com/login")

#Находим поле ввода логина
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    
#Вводим текст "tomsmith"
input_field.send_keys("tomsmith")

#Находим поле ввода пароля
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    
#Вводим текст "SuperSecretPassword!"
input_field.send_keys("SuperSecretPassword!")

search_locator = "button.radius"  
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys(Keys.RETURN) 

sleep(5)

#Закрываем браузер
driver.quit()