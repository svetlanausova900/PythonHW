from selenium import webdriver
from selenium.webdriver.edge.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#для EDGE запускаем драйвер на ПК и копируем порт
driver_url = "http://localhost:62544"

edge_options = Options()

driver = webdriver.Remote(
    command_executor=driver_url,
    options = edge_options
)


#открываем сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

#ожидание для загрузки
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3"))
    )

#вводим данные
input_field = driver.find_element(By.CSS_SELECTOR, "input[name='first-name']")
input_field.send_keys("Иван")


input_field = driver.find_element(By.CSS_SELECTOR, "input[name='last-name']")
input_field.send_keys("Петров")


input_field = driver.find_element(By.CSS_SELECTOR, "input[name='address']")
input_field.send_keys("Ленина, 55-3")


input_field = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']")
input_field.send_keys("test@skypro.com")

input_field = driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
input_field.send_keys("+7985899998787")


input_field = driver.find_element(By.CSS_SELECTOR, "input[name='city']")
input_field.send_keys("Москва")

#оставляем поле пустым
input_field = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']")
input_field.send_keys("")


input_field = driver.find_element(By.CSS_SELECTOR, "input[name='country']")
input_field.send_keys("Россия")


input_field = driver.find_element(By.CSS_SELECTOR, "input[name='job-position']")
input_field.send_keys("QA")

input_field = driver.find_element(By.CSS_SELECTOR, "input[name='company']")
input_field.send_keys("SkyPro")

#ищем кнопку Подтвердить и нажимаем ее
submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3")
submit_button.click()

#снова ищем каждый элемент, так как локатор изменился, и проверяем цвет в формате rgba. 
def get_background_color(element):
    return element.value_of_css_property("background-color")

zip_code = driver.find_element(By.ID, "zip-code")
zip_code_color = get_background_color(zip_code)
assert "rgba(248, 215, 218, 1)" == zip_code_color, f"Неверный цвет zip-code: {zip_code_color}"

first_name = driver.find_element(By.ID, "first-name")
first_name_color = get_background_color(first_name)
assert "rgba(209, 231, 221, 1)" == first_name_color, f"Неверный цвет first-name: {first_name_color}"

last_name = driver.find_element(By.ID, "last-name")
last_name_color = get_background_color(last_name)
assert "rgba(209, 231, 221, 1)" == last_name_color, f"Неверный цвет last_name: {last_name_color}"

address = driver.find_element(By.ID, "address")
address_color = get_background_color(address)
assert "rgba(209, 231, 221, 1)" == address_color, f"Неверный цвет address: {address_color}"

e_mail = driver.find_element(By.ID, "e-mail")
e_mail_color = get_background_color(e_mail)
assert "rgba(209, 231, 221, 1)" == e_mail_color, f"Неверный цвет e-mail: {e_mail_color}"

phone = driver.find_element(By.ID, "phone")
phone_color = get_background_color(phone)
assert "rgba(209, 231, 221, 1)" == phone_color, f"Неверный цвет phone: {phone_color}"

city = driver.find_element(By.ID, "city")
city_color = get_background_color(city)
assert "rgba(209, 231, 221, 1)" == city_color, f"Неверный цвет city: {city_color}"

country = driver.find_element(By.ID, "country")
country_color = get_background_color(country)
assert "rgba(209, 231, 221, 1)" == country_color, f"Неверный цвет country: {country_color}"

job_position = driver.find_element(By.ID, "job-position")
job_position_color = get_background_color(job_position)
assert "rgba(209, 231, 221, 1)" == job_position_color, f"Неверный цвет job-position: {job_position_color}"

company = driver.find_element(By.ID, "company")
company_color = get_background_color(company)
assert "rgba(209, 231, 221, 1)" == company_color, f"Неверный цвет company: {company_color}"


# Выводим True или False по итогу проверки цвета background. Для удобства снчала тот, что отличается от остальных
print(zip_code_color == "rgba(248, 215, 218, 1)")   
print(first_name_color == "rgba(209, 231, 221, 1)")  
print(last_name_color == "rgba(209, 231, 221, 1)") 
print(address_color == "rgba(209, 231, 221, 1)") 
print(e_mail_color == "rgba(209, 231, 221, 1)") 
print(phone_color == "rgba(209, 231, 221, 1)") 
print(country_color == "rgba(209, 231, 221, 1)") 
print(city_color == "rgba(209, 231, 221, 1)") 
print(job_position_color == "rgba(209, 231, 221, 1)") 
print(company_color == "rgba(209, 231, 221, 1)") 


driver.quit()



