import pytest
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage

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
    main_page.add_product_to_cart_by_name('Sauce Labs Backpack')
    main_page.add_product_to_cart_by_name('Sauce Labs Bolt T-Shirt')
    main_page.add_product_to_cart_by_name('Sauce Labs Onesisie')

    # Переход в корзину
    main_page.go_to_cart()

    # Нажатие на кнопку
    cart_page = CartPage(driver)
    cart_page.click_continue()

    # Заполнение формы данными
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_first_name('Алевтина')
    checkout_page.enter_last_name('Смирнова')
    checkout_page.enter_postal_code('198324')
    checkout_page.click_continue()

    # Проверить, что итоговая сумма равна $58.29
    assert total_price 'text' == "Total: $58.29"'