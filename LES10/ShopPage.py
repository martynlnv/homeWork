from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    """Page Object для главной страницы интернет-магазина."""

    def __init__(self, browser) -> None:
        """Инициализация главной страницы"""
        self.driver = browser
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    @allure.step("Добавление товаров в корзину")
    def add_items_to_cart(self) -> None:
        """Добавляем три тестовых товаров в корзину."""
        items = [
            "#add-to-cart-sauce-labs-backpack",
            "#add-to-cart-sauce-labs-bolt-t-shirt",
            "#add-to-cart-sauce-labs-onesie"
        ]
        for item in items:
            self.driver_find_element(By.CSS_SELECTOR, item).click()

    @allure.step("Ожидание и переход  в корзину")
    def wait_for_cart_item(self) -> None:
        """Ожидает появления иконки корзины и кликает по ней."""
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(
                (By.ID, "shopping_cart_container"))).click()


class LoginPage:
    """Page Object для страницы авторизации """
    def __init__(self, browser) -> None:
        """Инициализация страницы авторизации."""
        self.driver = browser

        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.driver.find_element(By.ID, 'user-name').send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, 'password').send_keys(password)

    def enter_login(self):
        self.driver.find_element(By.ID, 'login-button').click()


class CheckoutPage:
    """Page Object для страницы оформления заказа"""
    def __init__(self, browser) -> None:
        self.driver = browser

    @allure.step("Ввод имени")
    def enter_first_name_input(self) -> None:
        """Вводит имя в поле 'First Name'."""
        first_name_input = self.driver.find_element(By.ID, 'first-name')
        first_name_input.clear()
        first_name_input.send_keys('Алевтина')

    @allure.step("Ввод фамилии")
    def enter_last_name_input(self) -> None:
        """Вводит фамилию в поле 'Last Name'."""
        last_name_input = self.driver.find_element(By.ID, 'last-name')
        last_name_input.clear()
        last_name_input.send_keys('Смирнова')

    @allure.step("Ввод почтового индекса")
    def enter_postal_code(self) -> None:
        """Вводит почтовый индекс в поле 'Postal Code'."""
        postal_code_input = self.driver.find_element(By.ID, 'postal-code')
        postal_code_input.clear()
        postal_code_input.send_keys('198324')

    @allure.step("Нажатие кнопки продолжения")
    def click_continue(self) -> None:
        """Нажимает кнопку 'Continue' для перехода к следующему шагу."""
        continue_button = self.driver.find_element(By.ID, 'continue')
        continue_button.click()

    @allure.step("Получение итоговой суммы")
    def total_price(self) -> str:
        """
        Получает итоговую сумму заказа.

        Returns:
            str: Текст с итоговой суммой.
        """
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            ".summary_total_label")))
        total_price_element = self.driver.find_element(By.CSS_SELECTOR,
                                                       ".summary_total_label")
        return total_price_element.text


class CartPage:
    """Page Object для страницы корзины"""

    def __init__(self, browser):
        """Инициализация страницы корзины"""
        self.driver = browser
        self.driver.get("https://www.saucedemo.com/cart.html")

    @allure.step("Нажатие кнопки оформления заказа.")
    def click_continue(self) -> None:
        """Нажимает кнопку 'Checkout' для перехода к оформлению заказа."""
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    @allure.step("Проверка содержимого корзины.")
    def verify_cart(self) -> int:
        """
        Проверяет содержимое корзины.
        Returns:
             int: Количество элементов в корзине
        """
        cart_items = not (self.driver.find_elements(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").
                          find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").
                          find_elements(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").text)
        return int(cart_items)
