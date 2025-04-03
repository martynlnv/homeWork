from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# зайти на страницу
driver.get("http://the-internet.herokuapp.com/login")
sleep(2)

# в поле username ввести значение tomsmith
username_input = driver.find_element(By.XPATH, '//input[@type="text" and @name="username" and @id="username"]')
username_input.send_keys("tomsmith")
sleep(2)

# в поле password ввести значение SuperSecretPassword!
password_input = driver.find_element(By.XPATH, '//input[@type="password" and @name="password" and @id="password"]')
password_input.send_keys("SuperSecretPassword!")
sleep(2)

# нажать на кнопку Login
submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
submit_button.send_keys(Keys.RETURN)

#  вывести текст с зеленой плашки в консоль
flash = driver.find_element(By.CSS_SELECTOR, '#flash')
print(flash.text)

#  Закрыть браузер (метод  quite())
driver.quit()


