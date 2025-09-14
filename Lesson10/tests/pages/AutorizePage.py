from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Autorize:
    """Класс для авторизации на сайте Saucedemo"""
    
    def __init__(self, driver) -> None:
        """Инициализирует экземпляр класса с драйвером и настройками ожидания
        
        Args:
            driver: WebDriver -  экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.fields = {
            'user-name': "standard_user",
            'password': "secret_sauce"
        }

    def open(self) -> None:
        """Открывает страницу авторизации"""
        self.driver.get("https://www.saucedemo.com/")

    def fill_form(self) -> None:
        """Заполняет форму авторизации данными из словаря fields"""
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)
            
    def submit_form(self) -> None:
        """Отправляет форму авторизации"""
        self.wait.until(
            EC.element_to_be_clickable((
                (By.ID, "login-button")))).click()