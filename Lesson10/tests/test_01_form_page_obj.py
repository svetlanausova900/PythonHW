import allure
import pytest
from selenium import webdriver
from pages.FormPage import FormPage


@pytest.fixture
def driver():
    """Создает и настраивает экземпляр WebDriver для тестов"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver

    driver.quit()


@allure.title("Тест процесса отправки формы")
@allure.description("Тестирует полный процесс отправки формы: открытие, заполнение, отправка и проверка")
@allure.feature("Форма отправки данных")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission_flow(driver):
    """Тестирует полный процесс отправки формы: открытие, заполнение, отправка и проверка"""
    form_page = FormPage(driver)
    
    with allure.step("Открытие страницы с формой"):
        form_page.open()
    
    with allure.step("Заполнение формы данными"):
        form_page.fill_form()
    
    with allure.step("Отправка формы"):
        form_page.submit_form()
    
    with allure.step("Проверка успешной отправки формы"):
        form_page.check_form_submission()


@allure.step("Получение фонового цвета элемента")
def get_background_color(element):
    """Возвращает значение фонового цвета элемента"""
    return element.value_of_css_property("background-color")
