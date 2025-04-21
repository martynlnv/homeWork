from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self,  browser):
        self.driver =  browser
        self.username_input = ((By.ID, 'user-name').send_keys('standard_user')).click()
        self.password_input = (By.ID, 'password').send_keys('secret_sauce').click()
        self.login_button = (By.ID, 'login-button').send_keys('secret_sauce').click()


