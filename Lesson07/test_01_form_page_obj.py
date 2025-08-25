import pytest
from selenium import webdriver
from pages.FormPage import FormPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver

    driver.quit()


def test_form_submission_flow(driver):
    form_page = FormPage(driver)
    form_page.open()
    form_page.fill_form()
    form_page.submit_form()
    form_page.check_form_submission()

def get_background_color(element):
    return element.value_of_css_property("background-color")

