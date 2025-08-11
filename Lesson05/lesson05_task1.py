from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# # Отключаем предупреждения
# import requests
# from urllib3.exceptions import InsecureRequestWarning

# requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# response = requests.get('https://uitestingplayground.com/classattr', verify=False)
# print(response.text)



driver.get("https://uitestingplayground.com/classattr")

blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
blue_button.click()
    
# Обработать алерт (если появится)
alert = driver.switch_to.alert
alert.accept()
    
sleep(5)