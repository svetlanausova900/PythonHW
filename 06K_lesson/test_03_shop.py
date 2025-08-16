from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Инициализация драйвера Firefox
driver = webdriver.Firefox()

#Переход на страницу
driver.get("https://www.saucedemo.com/")
    
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )

#Логинимся
input_field = driver.find_element(By.ID, "user-name")
input_field.send_keys("standard_user")
input_field = driver.find_element(By.ID, "password")
input_field.send_keys("secret_sauce")
input_field = driver.find_element(By.ID, "login-button")
input_field.click()

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))
    )

#добавляем товары

input_field = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
input_field.click()

input_field = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
input_field.click()

input_field = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
input_field.click()

#переходим в корзину
input_field = driver.find_element(By.ID, "shopping_cart_container")
input_field.click()

input_field = driver.find_element(By.ID, "checkout")
input_field.click()

#вводим данные
input_field = driver.find_element(By.ID, "first-name")
input_field.send_keys("Svetlana")
input_field = driver.find_element(By.ID, "last-name")
input_field.send_keys("Usova")
input_field = driver.find_element(By.ID, "postal-code")
input_field.send_keys("193255")
input_field = driver.find_element(By.ID, "continue")
input_field.click()

#Ищем общую стоимость, отделяем от Тотал и $. Выводим в терминал
input_field = driver.find_element(By.XPATH, '//div[@class="summary_total_label"]')
text = input_field.text
total = text.split("$")[-1]
print(total)

driver.quit()

#проверяем результат
expected_result = "58.29"
assert total == expected_result, f"Ожидалось: 58.29, получено: {total}"

#выводим сообщение об успешном тесте
print("Итоговая стоимость равна ожидаемой. Тест пройден!")

