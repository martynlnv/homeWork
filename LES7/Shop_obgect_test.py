import pytest
from selenium import webdriver
from ShopPage import *

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_purchases(driver):
    # Авторизация
    login_page = LoginPage(driver)
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    login_page.enter_login()

    # Добавление товаров в корзину
    main_page = MainPage(driver)
    main_page.add_items_to_cart()

    # Переход в корзину
    main_page.wait_for_cart_item()

    # Нажатие на кнопку
    cart_page = CartPage(driver)
    cart_page.click_continue()

    # Заполнение формы данными
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_first_name_input()
    checkout_page.enter_last_name_input()
    checkout_page.enter_postal_code()
    checkout_page.click_continue()

    # Проверить, что итоговая сумма равна $58.29
    assert checkout_page.total_price() == "Total: $58.29"