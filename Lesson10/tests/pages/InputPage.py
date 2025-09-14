from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Input:
    """Класс для работы с формой ввода данных"""
    
    def __init__(self, driver) -> None:
        """Инициализирует экземпляр класса с драйвером, настройками ожидания и данными для заполнения
        
        Args:
            driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.fields = {
            'first-name': "Svetlana",
            'last-name': "Usova",
            'postal-code': "193255"
        }

    def fill_field(self, field_id: str, value: str) -> None:
        """Заполняет указанное поле формы заданным значением
        
        Args:
            field_id: str - ID поля для заполнения
            value: str - значение для ввода
        """
        element = self.wait.until(
            EC.presence_of_element_located((By.ID, field_id))
        )
        element.clear()
        element.send_keys(value)
    
    def fill_all_fields(self) -> None:
        """Заполняет все поля формы данными из словаря fields"""
        for field_id, value in self.fields.items():
            self.fill_field(field_id, value)
            
    def submit_form(self) -> None:
        """Отправляет заполненную форму"""
        self.wait.until(
            EC.element_to_be_clickable((
                (By.ID, "continue")))).click() 
        
    def get_total_price(self) -> str:
        """Возвращает общую стоимость из элемента на странице
        
        Returns:
            str - текст с общей стоимостью
        """
        total_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="summary_total_label"]'))
        )
        return total_element.text