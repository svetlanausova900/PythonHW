from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class Cart:
    """Класс для работы с корзиной покупок"""
    
    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует экземпляр класса с драйвером и настройками ожидания
        
        Args:
            driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    """Локаторы элементов корзины"""
    CART_BUTTON = (By.ID, "shopping_cart_container")
    CHECKOUT_BUTTON = (By.ID, "checkout")
        
    def go_to_cart(self) -> 'Cart':
        """Переходит в корзину покупок
        
        Returns:
            Cart - текущий  экземпляр класса для цепочки вызовов
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CART_BUTTON)
        ).click()
        return self

    def go_to_checkout(self) -> 'Cart':
        """Переходит к оформлению заказа
        
        Returns:
            Cart - текущий экземпляр класса для цепочки вызовов
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()
        return self 

