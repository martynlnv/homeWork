import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_validation(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, 'first-name').send_keys('Иван')
    driver.find_element(By.NAME, 'last-name').send_keys('Петров')
    driver.find_element(By.NAME, 'address').send_keys('Ленина, 55-3')
    driver.find_element(By.NAME, 'e-mail').send_keys('test@skypro.com')
    driver.find_element(By.NAME, 'phone').send_keys('+7985899998787')
    driver.find_element(By.NAME, 'zip-code').send_keys('')
    driver.find_element(By.NAME, 'city').send_keys('Москва')
    driver.find_element(By.NAME, 'country').send_keys('Россия')
    driver.find_element(By.NAME, 'job-position').send_keys('QA')
    driver.find_element(By.NAME, 'company').send_keys('SkyPro')

    # нажать на кнопку submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    driver.implicitly_wait(5)

# подсветка красным поля Zip
    zip_code_field = driver.find_element(By.CSS_SELECTOR, '#zip-code')
    assert 'alert-danger' in zip_code_field.get_attribute('class'), \
        'Поле Zip code не подсвечено красным'

# подсветка остальных полей зеленым
    fields_to_check = {
        'first-name': 'success',
        'last-name': 'success',
        'address': 'success',
        'e-mail': 'success',
        'phone': 'success',
        'city': 'success',
        'country': 'success',
        'job-position': 'success',
        'company': 'success',
        }

    for name, expected_class in fields_to_check.items():
        field = driver.find_element(By.ID, name)

    assert expected_class in field.get_attribute('class'), \
        f'Поле {name} не подсвечено зеленым'
