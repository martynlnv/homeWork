from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    """Page Object для страницы калькулятора"""

    def __init__(self,  browser: webdriver.Chrome):
        """
        Инициализация страницы.
        :param browser: Экземпляр WebDriver (Chrome).
        """
        self.driver = browser
        self.driver.get(
            'https://'
            'bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
            )
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    @allure.step("Установить задержку калькулятора в {seconds} секунд")
    def set_delay(self, seconds: int) -> None:
        """
         Устанавливает задержку вычислений.

        :param seconds: Число секунд (целое число)
        """
        input_field = self.driver.find_element(By.ID, 'delay')
        input_field.clear()
        input_field.send_keys(seconds)

    @allure.step("Нажать на кнопку '{button}'")
    def click_button(self, button: str) -> None:
        self.driver.find_element(
            By.XPATH, f'//span[text() = "{button}"]').click()

    @allure.step("Дождаться результата '{expected_result}'")
    def wait_result(self, result: str) -> None:
        """
        Ожидает появления результата на экране.
        :param result: Ожидаемый результат (например, "15").
        """
        wait = WebDriverWait(self.driver, 46)
        wait.until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".screen"), result))
