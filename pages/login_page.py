from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.NAME, 'user-name')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.NAME, 'login-button')

    def navigate_login(self):
        self.navigate_to("https://www.saucedemo.com")

    def click_login(self):
        self.click(self.LOGIN_BUTTON)