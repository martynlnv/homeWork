from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#зайти на сайт
driver.get("http://uitestingplayground.com/dynamicid")

# кликнуть на синюю кнопку
driver.find_element(By.XPATH,"//button[contains(text(), 'Button with Dynamic ID')]").click()
driver.quit()

sleep(5)

