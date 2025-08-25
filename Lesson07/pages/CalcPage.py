from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.implicitly_wait(4)
   
        
    def set_delay(self, delay_value):
        delay_field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(str(delay_value))
    
        
    def click_button(self, button_text):
        button = self.driver.find_element(By.XPATH, f"//span[text()='7']")
        button.click()
        
    def get_result(self):
        result_field = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return result_field.text
        
    def wait_for_result(self, timeout=50):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(
            lambda driver: self.get_result() != '0' and self.get_result() != ''
        )
        
    def calculate(self, expression, delay=45):
        self.set_delay(delay)
        
        for char in expression:
            if char.isdigit() or char in ['+', '-', '*', '/', '=']:
                self.click_button(char)
                
        self.wait_for_result()
        return self.get_result()
    
    