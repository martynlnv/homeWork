from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, browser):
        self.driver = browser
        self.driver.implicitly_wait(4)

    # Добавляем товары в корзину
    def add_items_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    # Ожидание появления товара в корзине
    def wait_for_cart_item(self):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "shopping_cart_container"))).click()


class LoginPage:
    def __init__(self, browser):
        self.driver = browser
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.driver.find_element(By.ID, 'user-name').send_keys(username)
    def enter_password(self, password):
        self.driver.find_element(By.ID, 'password').send_keys(password)
    def enter_login(self):
        self.driver.find_element(By.ID, 'login-button').click()

class CheckoutPage:
    def __init__(self, browser):
        self.driver = browser


    def enter_first_name_input(self):
        first_name_input = self.driver.find_element(By.ID, 'first-name')
        first_name_input.clear()
        first_name_input.send_keys('Алевтина')

    def enter_last_name_input(self):
        last_name_input = self.driver.find_element(By.ID, 'last-name')
        last_name_input.clear()
        last_name_input.send_keys('Смирнова')


    def enter_postal_code(self):
        postal_code_input = self.driver.find_element(By.ID, 'postal-code')
        postal_code_input.clear()
        postal_code_input.send_keys('198324')

    def click_continue(self):
        continue_button = self.driver.find_element(By.ID, 'continue')
        continue_button.click()


    def total_price(self):
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
        total_price_element = self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
        return total_price_element.text

class CartPage:

    def __init__(self, browser):
        self.driver = browser
        self.driver.get("https://www.saucedemo.com/cart.html")
    def click_continue(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()


    # Проверка содержимого корзины
    def verify_cart(self):
        cart_items = not self.driver.find_elements(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").find_elements(By.CSS_SELECTOR,
                                                                                   "#add-to-cart-sauce-labs-onesie").text
        return int(cart_items)

