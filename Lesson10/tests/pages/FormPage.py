from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    """Класс для работы с формой заполнения данных"""
    
    def __init__(self, driver) -> None:
        """Инициализирует экземпляр класса с драйвером, настройками ожидания и данными для заполнения
        
        Args:
            driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    def open(self) -> None:
        """Открывает страницу с формой для заполнения"""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
            )

    def fill_form(self) -> None:
        """Заполняет все поля формы данными из словаря fields"""
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)

    def submit_form(self) -> None:
        """Отправляет заполненную форму"""
        self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '[type="submit"]'))).click()

    def get_field_class(self, field_id: str) -> str:
        """Возвращает CSS класс указанного поля формы
  
        Args:
            field_id: str - ID поля формы
            
        Returns:
            str - CSS класс поля
        """
        element = self.wait.until(
            EC.presence_of_element_located((
                By.ID, field_id))).get_attribute("class")
        return element

    def check_zip_code_error(self) -> bool:
        """Проверяет наличие ошибки у поля zip-code
        
        Returns:
            bool - True если есть ошибка, False если нет
        """
        return "alert-danger" in self.get_field_class("zip-code")

    def check_fields_success(self) -> bool:
        """Проверяет успешное заполнение всех обязательных полей формы
        
        Returns:
            bool - True если все поля успешно заполнены, False если есть ошибки
        """
        fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone',
                  'city', 'country', 'job-position', 'company']
        for field in fields:
            if "success" not in self.get_field_class(field):
                return False
        return True

    def check_form_submission(self) -> None:
        """Проверяет результат отправки формы: наличие ошибки у zip-code и успех у остальных полей"""
        assert self.check_zip_code_error()
        assert self.check_fields_success()



        