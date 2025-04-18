from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class CartPage:

    def __init__(self, browser):
        self.driver = browser
        self.driver.get("https://www.saucedemo.com/cart.html")
        self.checkout_button = (By.CSS_SELECTOR, "#checkout")
        self.expected_items = expected_items

    # Проверка содержимого корзины
    def verify_cart(self):
        cart_items = not self.driver.find_elements(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").find_elements(By.CSS_SELECTOR,
                                                                                   "#add-to-cart-sauce-labs-onesie").text
        return int(cart_items)

