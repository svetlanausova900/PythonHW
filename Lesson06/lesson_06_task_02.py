from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "newButtonName"))
    )

input_field = driver.find_element(By.ID, "newButtonName")
    

input_field.send_keys("SkyPro")

blue_button = driver.find_element(By.ID, "updatingButton")
blue_button.click()

print(WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
))

print(driver.find_element(By.ID, "updatingButton").text )

driver.quit()

