import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator_delay(driver):
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

# Вводим значение 45 в поле ввода delay
    delay_input = driver.find_element(By.ID, 'delay')
    delay_input.clear()
    delay_input.send_keys('5')

# Нажимаем кнопки 7 + 8 =
    driver.find_element(By.XPATH, '//span[text() = "7"]').click()
    driver.find_element(By.XPATH, '//span[text() = "+"]').click()
    driver.find_element(By.XPATH, '//span[text() = "8"]').click()
    driver.find_element(By.XPATH, '//span[text() = "="]').click()

# Ждем появления результата
    WebDriverWait(driver, 46).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
    assert driver.find_element(By.CSS_SELECTOR, ".screen").text == "15"
