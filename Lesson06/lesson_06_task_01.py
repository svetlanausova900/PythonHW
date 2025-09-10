from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ajaxButton"))
    )

driver.find_element(By.ID, "updatingButton").click()

print(driver.find_element(By.CSS_SELECTOR, ".bg-success").text )

driver.quit()