import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from CalculatorPage import CalculatorPage
import allure


@pytest.fixture
def driver():
    """Фикстура для инициализации и завершения работы драйвера"""
    with allure.step("Открыть браузер и перейти на страницу калькулятора"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        yield driver
        driver.quit()


@allure.title("Проверка вычислений с задержкой")
@allure.description(
    "Проверка корректности работы калькулятора"
    " с установленной задержкой вычислений"
                    )
@allure.feature("Калькулятор с задержкой")
@allure.severity("CRITICAL")
def test_calculate_delay(driver):
    """Тест проверяет работу калькулятора с задержкой."""
    calculator_page = CalculatorPage(driver)

    with allure.step("Установить задержку 45 секунд"):
        calculator_page.set_delay(45)

    with allure.step("Выполнить вычисление 7 + 8 = 15"):
        calculator_page.click_button("7")
        calculator_page.click_button("+")
        calculator_page.click_button("8")
        calculator_page.click_button("=")

    with allure.step("Проверить результат"):
        calculator_page.wait_result("15")
        assert driver.find_element(By.CSS_SELECTOR, ".screen").text == "15"
