from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

#зайти на сайт
driver.get("http://the-internet.herokuapp.com/inputs")
sleep(4)
# ввести в поле текст 1000
number_input = driver.find_element(By.XPATH,'//input[@type="number"]')
number_input.send_keys("1000", Keys.RETURN)
sleep(4)
# Очистить это поле (метод clear())
number_input.clear()

# Ввести в поле текст 999
number_input = driver.find_element(By.XPATH, '//input[@type="number"]')
number_input.send_keys("999", Keys.RETURN)
sleep(4)
# Закрыть браузер (метод  quite())
driver.quit()


