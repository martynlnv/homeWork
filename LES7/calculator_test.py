import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from calculatorPage import CalculatorPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    yield driver
    driver.quit()

def test_calculate_delay(browser):
    calculator_page = CalculatorPage(browser)
    calculator_page.set_delay(46)
    calculator_page.click_button()

    calculator_page.wait_result(15)
    assert driver.find_element(By.CSS_SELECTOR, ".screen").text == "15"