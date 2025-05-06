from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https:www.labirint.ru/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def set_cookie_policy(self):
        cookie = {
            "name":"cookie_polycy",
            "value":"1"
        }

        self.driver.add_cookie(cookie)
        print('меня вызвали')

    def search(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()