import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False})
driver = webdriver.Chrome(options=chrome_options)
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.AutorizePage import Autorize
from pages.ShopListPage import ShopList
from pages.CartPage import Cart
from pages.InputPage import Input

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def authorized_driver(driver):
    auth_page = Autorize(driver)
    auth_page.open()
    auth_page.fill_form()
    auth_page.submit_form()
    return driver

def test_add_items_to_cart(authorized_driver):
    shop_page = ShopList(authorized_driver)
    shop_page.add_items_to_cart()


def test_go_to_cart(authorized_driver):
    shop_page = ShopList(authorized_driver)
    shop_page.add_items_to_cart()
    shop_page.go_to_cart()

    cart_page = Cart(authorized_driver)
    cart_page.go_to_checkout()

def test_input_driver(authorized_driver):

    shop_page = ShopList(authorized_driver)
    shop_page.add_items_to_cart()
    shop_page.go_to_cart()

    cart_page = Cart(authorized_driver)
    cart_page.go_to_checkout()

    in_page = Input(authorized_driver)
    in_page.fill_all_fields()
    in_page.submit_form()

def test_check_driver(authorized_driver):

    shop_page = ShopList(authorized_driver)
    shop_page.add_items_to_cart()
    shop_page.go_to_cart()

    cart_page = Cart(authorized_driver)
    cart_page.go_to_checkout()

    in_page = Input(authorized_driver)
    in_page.fill_all_fields()
    in_page.submit_form()
    
    total_text = in_page.get_total_price()
    expected_total = "Total: $58.29"
    
    assert total_text == expected_total, f"Ожидалось: {expected_total}, Получено: {total_text}"
    