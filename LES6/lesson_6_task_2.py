from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# перейти на сайт
driver.get('http://uitestingplayground.com/textinput')

# указать в поле ввода текст SkyPro
newButton_input = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
newButton_input.send_keys('SkyPro')

# нажать на синюю кнопку
driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()

# получить текст и вывести в консоль("SkyPro")
updated_button = WebDriverWait(driver, 16).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR,
'#updatingButton'), 'SkyPro'))

print(driver.find_element(By.CSS_SELECTOR, '#updatingButton').text)
driver.quit()
