from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class ShopList:
    """Класс для работы со списком товаров и корзиной покупок"""
    
    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует экземпляр класса с драйвером и настройками ожидания
        
        Args:
            driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, by: By, value: str) -> None:
        """Кликает на элемент, ожидая его кликабельности
        
        Args:
            by: By - стратегия поиска элемента
            value: str - значение для поиска элемента
        """
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()
      
    """Локаторы элементов для добавления товаров в корзину"""
    ADD_TO_CART_BACKPACK = (By.ID, 'add-to-cart-sauce-labs-backpack')
    ADD_TO_CART_BOLT_TSHIRT = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    ADD_TO_CART_ONESIE = (By.ID, 'add-to-cart-sauce-labs-onesie')
    CART_BUTTON = (By.CLASS_NAME, 'shopping_cart_link')
    
    def add_items_to_cart(self) -> None:
        """Добавляет все указанные товары в корзину"""
        self.click_element(*self.ADD_TO_CART_BACKPACK)
        self.click_element(*self.ADD_TO_CART_BOLT_TSHIRT)
        self.click_element(*self.ADD_TO_CART_ONESIE)
    
    def go_to_cart(self) -> 'ShopList':
        """Переходит в корзину покупок
        
        Returns:
            ShopList - текущий экземпляр класса для цепочки вызовов
        """
        self.click_element(*self.CART_BUTTON)
        return self
