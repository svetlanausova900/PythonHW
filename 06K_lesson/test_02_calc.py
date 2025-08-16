from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

#открываем сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

#ожидание для загрузки
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "calculator"))
    )

#вводим данные
input_field = driver.find_element(By.ID, "delay")
input_field.clear()
input_field.send_keys("45")

input_field = driver.find_element(By.XPATH, "//span[text()='7']")
input_field.click()

input_field = driver.find_element(By.XPATH, "//span[text()='+']")
input_field.click()

input_field = driver.find_element(By.XPATH, "//span[text()='8']")
input_field.click()

input_field = driver.find_element(By.XPATH, "//span[text()='=']")
input_field.click()

#просим драйвер подождать 50 секуд, чтобы отображен был результат
result = WebDriverWait(driver, 50).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
)

#ищем результат
result_element = driver.find_element(By.CLASS_NAME, "screen")

#проверяем результат
expected_result = "15"
assert result_element.text == expected_result, f"Ожидалось: 15, получено: {result_element.text}"

#выводим сообщение об успешном тесте
print("Тест пройден! Отображается правильное значение.")


driver.quit()


