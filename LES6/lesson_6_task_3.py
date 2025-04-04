from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')


img = WebDriverWait(driver, 10)
img.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#text'), "Done!")
)
# идем по ветке
div = driver.find_element(By.CSS_SELECTOR, "#image-container")

# ищем все элементы
imgs = driver.find_elements(By.CSS_SELECTOR, 'img')
img = imgs[3]

# запрашиваем атрибуты и помещаем в переменную src
src = img.get_attribute('src')
print(src)
driver.quit()
