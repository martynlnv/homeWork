import pytest
from selenium import webdriver
from ShopPage import *
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

    @allure.title("Процесс покупки товаров.")
    @allure.description("Проверка полного цикла покупки:"
                        " авторизация, добавление товаров, оформление заказа.")
    @allure.feature("Покупки в интернет-магазине.")
    @allure.severity("CRITICAL")
    def test_purchases(driver):
        with allure.step("Авторизация пользователя"):
            login_page = LoginPage(driver)
            login_page.enter_username('standard_user')
            login_page.enter_password('secret_sauce')
            login_page.enter_login()

        with allure.step("Добавление товаров в корзину"):
            main_page = MainPage(driver)
            main_page.add_items_to_cart()

        with allure.step("Переход в корзину"):
            main_page.wait_for_cart_item()

        with allure.step("Начало оформления заказа, нажатие на кнопку"):
            cart_page = CartPage(driver)
            cart_page.click_continue()

        with allure.step("Заполнение формы данными"):
            checkout_page = CheckoutPage(driver)
            checkout_page.enter_first_name_input()
            checkout_page.enter_last_name_input()
            checkout_page.enter_postal_code()
            checkout_page.click_continue()

        with allure.step("Проверка, что итоговая сумма равна $58.29"):
            assert checkout_page.total_price() == "Total: $58.29"
