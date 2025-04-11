import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_buy_items_and_check_total(driver):
    driver.get('https://www.saucedemo.com/')

    # Авторизация
    username_field = driver.find_element(By.ID, 'user-name')
    password_field = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-button')

    username_field .send_keys('standard_user')
    password_field.send_keys('secret_sauce')
    login_button.click()

    # Добавление товаров в корзину
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    # Переход в корзину
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    # Нажать Checkout
    driver.find_element(
        By.XPATH, "//button[@id='checkout' and @data-test='checkout']").click()

    # Заполнить форму данными
    driver.find_element(By.ID, 'first-name').send_keys('Алевтина')
    driver.find_element(By.ID, 'last-name').send_keys('Смирнова')
    driver.find_element(By.ID, 'postal-code').send_keys("198324")
    driver.find_element(By.ID, 'continue').click()


# Прочитайте со страницы итоговую стоимость (Total)
    total_element = driver.find_element(
        By.XPATH, "//div[@class='summary_total_label' and @data-test='total-label']")
    text = total_element.text

    # Проверьте, что итоговая сумма равна $58.29

    assert text == "Total: $58.29"
