from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopList:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, by, value):
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()
      
    ADD_TO_CART_BACKPACK = (By.ID, 'add-to-cart-sauce-labs-backpack')
    ADD_TO_CART_BOLT_TSHIRT = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    ADD_TO_CART_ONESIE = (By.ID, 'add-to-cart-sauce-labs-onesie')
    CART_BUTTON = (By.CLASS_NAME, 'shopping_cart_link')
    
    def add_items_to_cart(self):
        self.click_element(*self.ADD_TO_CART_BACKPACK)
        self.click_element(*self.ADD_TO_CART_BOLT_TSHIRT)
        self.click_element(*self.ADD_TO_CART_ONESIE)
    
    def go_to_cart(self):
        self.click_element(*self.CART_BUTTON)
        return self