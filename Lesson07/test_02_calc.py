import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.CalcPage import CalcPage
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calculation_with_delay(driver):
    # Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    # Устанавливаем задержку
    delay_field = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_field.clear()
    delay_field.send_keys("45")
    
    # Нажимаем кнопки
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()
    
    # Ждем результат
    start_time = time.time()
    
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


