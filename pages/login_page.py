from selenium.webdriver.common.by import By
from .base_page import BasePage
from assets.config import USERNAME, PASSWORD

class LoginPage(BasePage):
    USERNAME_INPUT = (By.NAME, 'user-name')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.NAME, 'login-button')
    USERNAME_REQUIRED_ERROR_MESSAGE = (By.XPATH, '//h3[@data-test="error" and text()="Epic sadface: Username is required"]')

    def navigate_login(self):
        self.navigate_to("https://www.saucedemo.com")
    
    def enter_credentials(self, username, password):
        self.click(self.USERNAME_INPUT)
        self.type_text(self.USERNAME_INPUT, username)
        self.click(self.PASSWORD_INPUT)
        self.type_text(self.PASSWORD_INPUT,password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
    
    def message_error_is_displayed(self, locator):
        error_element = self.wait_for_element(locator)
        return error_element.is_displayed()

    def login(self):
        self.navigate_to("https://www.saucedemo.com")
        self.enter_credentials(USERNAME, PASSWORD)
        self.click_login()        