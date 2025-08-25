from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Autorize:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.fields = {
            'user-name': "standard_user",
            'password': "secret_sauce"
        }

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def fill_form(self):
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)
            
    def submit_form(self):
        self.wait.until(
            EC.element_to_be_clickable((
                (By.ID, "login-button")))).click() 
