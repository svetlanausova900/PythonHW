import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pages.AutorizePage import Autorize
from pages.ShopListPage import ShopList
from pages.CartPage import Cart
from pages.InputPage import Input


@pytest.fixture
def driver():
    """Создает и настраивает экземпляр WebDriver для тестов"""
    with allure.step("Инициализация WebDriver Chrome"):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    with allure.step("Максимизация окна браузера"):
        driver.maximize_window()
    
    yield driver
    
    with allure.step("Завершение работы WebDriver"):
        driver.quit()


@allure.title("Тестирование калькулятора с задержкой вычислений")
@allure.description("Тест проверяет работу калькулятора с установленной задержкой 45 секунд. "
                   "Проверяет корректность вычисления 7 + 8 = 15 с ожиданием результата.")
@allure.feature("Калькулятор с задержкой")
@allure.severity(allure.severity_level.NORMAL)
def test_calculation_with_delay(driver):
    with allure.step("Открытие страницы калькулятора"):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        allure.attach(driver.get_screenshot_as_png(), name="Страница калькулятора", 
                     attachment_type=allure.attachment_type.PNG)
    
    with allure.step("Установка задержки вычислений в 45 секунд"):
        delay_field = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys("45")
        allure.attach(f"Установлена задержка: 45 секунд", name="Задержка", 
                     attachment_type=allure.attachment_type.TEXT)
    
    with allure.step("Выполнение операции сложения: 7 + 8"):
        with allure.step("Нажатие кнопки '7'"):
            driver.find_element(By.XPATH, "//span[text()='7']").click()
        
        with allure.step("Нажатие кнопки '+'"):
            driver.find_element(By.XPATH, "//span[text()='+']").click()
        
        with allure.step("Нажатие кнопки '8'"):
            driver.find_element(By.XPATH, "//span[text()='8']").click()
        
        with allure.step("Нажатие кнопки '='"):
            driver.find_element(By.XPATH, "//span[text()='=']").click()
        
        allure.attach(driver.get_screenshot_as_png(), name="Ввод операции", 
                     attachment_type=allure.attachment_type.PNG)
    
    with allure.step("Ожидание результата вычислений с таймаутом 50 секунд"):
        start_time = time.time()
        
        result = WebDriverWait(driver, 50).until(
           EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        allure.attach(f"Время ожидания результата: {execution_time:.2f} секунд", 
                     name="Время выполнения", attachment_type=allure.attachment_type.TEXT)
        
        allure.attach(driver.get_screenshot_as_png(), name="Результат вычислений", 
                     attachment_type=allure.attachment_type.PNG)
    
    with allure.step("Проверка корректности результата"):
        result_element = driver.find_element(By.CLASS_NAME, "screen")
        expected_result = "15"
        actual_result = result_element.text
        
        assert actual_result == expected_result, f"Ожидалось: {expected_result}, получено: {actual_result}"
        
        allure.attach(f"Ожидаемый результат: {expected_result}\nФактический результат: {actual_result}", 
                     name="Результаты проверки", attachment_type=allure.attachment_type.TEXT)
    
    with allure.step("Тест успешно завершен"):
        print("Тест пройден! Отображается правильное значение.")
        allure.attach("Тест пройден успешно! Отображается правильное значение.", 
                     name="Статус теста", attachment_type=allure.attachment_type.TEXT)