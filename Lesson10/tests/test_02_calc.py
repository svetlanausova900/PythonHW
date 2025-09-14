import pytest
import allure
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
    """Создает и настраивает экземпляр WebDriver для тестов"""
    with allure.step("Инициализация WebDriver"):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        yield driver
        with allure.step("Закрытие браузера"):
            driver.quit()


@allure.title("Тест калькулятора с задержкой")
@allure.description("Тестирует работу калькулятора с установленной задержкой 45 секунд")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calculation_with_delay(driver):
    with allure.step("Открываем страницу калькулятора"):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    with allure.step("Устанавливаем задержку 45 секунд"):
        delay_field = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys("45")
    
    with allure.step("Выполняем операцию 7 + 8"):
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()
    
    with allure.step("Ожидаем результат с таймаутом 50 секунд"):
        start_time = time.time()
        
        result = WebDriverWait(driver, 50).until(
           EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        end_time = time.time()
        
        execution_time = end_time - start_time
        allure.attach(f"Время выполнения операции: {execution_time:.2f} секунд", 
                     name="Время выполнения", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Проверяем результат вычислений"):
        result_element = driver.find_element(By.CLASS_NAME, "screen")
        expected_result = "15"
        
        assert result_element.text == expected_result, f"Ожидалось: {expected_result}, получено: {result_element.text}"
        
        allure.attach(f"Ожидаемый результат: {expected_result}\nФактический результат: {result_element.text}", 
                     name="Результаты проверки", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Тест успешно пройден"):
        print("Тест пройден! Отображается правильное значение.")
        allure.attach("Тест пройден успешно! Отображается правильное значение.", 
                     name="Статус теста", attachment_type=allure.attachment_type.TEXT)


