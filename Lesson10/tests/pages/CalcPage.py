from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class CalcPage:
    """Класс для работы с калькулятором на веб-странице"""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует калькулятор: открывает страницу и настраивает параметры
        
        Args:
            driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.implicitly_wait(4)
   
    def set_delay(self, delay_value: int) -> None:
        """Устанавливает значение задержки для вычислений
        
        Args:
            delay_value: int - значение задержки в секундах
        """
        delay_field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(str(delay_value))
    
    def click_button(self, button_text: str) -> None:
        """Нажимает кнопку калькулятора с указанным текстом
        
        Args:
            button_text: str - текст на кнопке
        """
        button = self.driver.find_element(By.XPATH, f"//span[text()='7']")
        button.click()
        
    def get_result(self) -> str:
        """Возвращает текущий результат с экрана калькулятора
        
        Returns:
            str - текст результата вычислений
        """
        result_field = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return result_field.text
        
    def wait_for_result(self, timeout: int = 50) -> bool:
        """Ожидает появления результата вычислений в течение указанного времени
        
        Args:
            timeout: int - время ожидания в секундах (по умолчанию 50)
            
        Returns:
            bool - True если результат появился, иначе исключение TimeoutException
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(
            lambda driver: self.get_result() != '0' and self.get_result() != ''
        )
        
    def calculate(self, expression: str, delay: int = 45) -> str:
        """Выполняет вычисление выражения с указанной задержкой
        
        Args:
            expression: str - математическое выражение для вычисления
            delay: int - задержка вычислений в секундах (по умолчанию 45)
             
        Returns:
            str - результат вычислений
        """
        self.set_delay(delay)
        
        for char in expression:
            if char.isdigit() or char in ['+', '-', '*', '/', '=']:
                self.click_button(char)
                
        self.wait_for_result()
        return self.get_result()
     