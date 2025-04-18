from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:

    def __init__(self,  browser):
        self.driver = browser
        self.driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def set_delay(self, seconds):
        input_field = self.driver.find_element(By.ID, 'delay')
        input_field.clear()
        input_field.send_keys(seconds('46'))

    def click_button(self, expression):
        button = self.driver.find_element(expression)
        button.click()
        self.click_button(By.XPATH, '//span[text() = "7"]')
        self.click_button(By.XPATH, '//span[text() = "+"]')
        self.click_button(By.XPATH, '//span[text() = "8"]')
        self.click_button(By.XPATH, '//span[text() = "="]')

    def wait_result(self, result):
        wait = WebDriverWait(self.driver, 46)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), result))



