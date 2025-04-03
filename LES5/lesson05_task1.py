from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#зайти на сайт
driver.get(" http://uitestingplayground.com/classattr")

sleep(5)

# кликнуть на синюю кнопку
driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
driver.quit()

sleep(5)
